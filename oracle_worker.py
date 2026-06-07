import time
import requests
import hashlib
import json
import datetime
import sqlite3
import random
from logger import AlphaEngineLogger

# Configuration
NWS_API = "https://api.weather.gov/stations/{}/observations/latest"
HEADERS = {"User-Agent": "(TheUndesirablesOracle, contact@the-undesirables.com)"}
TARGET_STATIONS = [
    "KNYC", # New York (Central Park)
    "KORD", # Chicago (O'Hare)
    "KLAX", # Los Angeles
    "KMIA", # Miami
    "KIAH", # Houston
    "KDFW", # Dallas
    "KSEA", # Seattle
    "KATL", # Atlanta
    "KBOS", # Boston
    "KDCA"  # Washington DC
]
DB_PATH = "alpha_engine.sqlite"

logger = AlphaEngineLogger(db_path=DB_PATH)

def fetch_nws_data(station_id):
    """Fetches real-time weather from the National Weather Service."""
    try:
        res = requests.get(NWS_API.format(station_id), headers=HEADERS, timeout=10)
        res.raise_for_status()
        data = res.json()
        props = data.get("properties", {})
        
        # Parse NWS standard formatting
        temp_c = props.get("temperature", {}).get("value")
        temp_f = (temp_c * 9/5) + 32 if temp_c is not None else None
        
        precip = props.get("precipitationLastHour", {}).get("value", 0.0)
        wind_kmh = props.get("windSpeed", {}).get("value")
        wind_mph = wind_kmh * 0.621371 if wind_kmh is not None else None
        
        return {
            "city": station_id,
            "temp": round(temp_f, 2) if temp_f else 0.0,
            "precip": round(precip, 2) if precip else 0.0,
            "wind": round(wind_mph, 2) if wind_mph else 0.0
        }
    except Exception as e:
        print(f"[{datetime.datetime.now()}] ERROR fetching NWS for {station_id}: {e}")
        return None

def generate_merkle_root(payloads):
    """Mocks generating a Merkle Root from the combined observation payloads."""
    payload_str = json.dumps(payloads, sort_keys=True)
    return hashlib.sha256(payload_str.encode('utf-8')).hexdigest()

def mock_shroomy_engine(nws_data):
    """Mocks proprietary edge detection algorithm for Kalshi."""
    # Dummy logic: if temp is high, rain prob is low.
    market_id = f"KALSHI-{nws_data['city']}-RAIN-TODAY"
    kalshi_price = round(random.uniform(0.1, 0.9), 2)
    model_prob = round(random.uniform(0.1, 0.9), 2)
    
    # Kelly bet simulation
    edge = model_prob - kalshi_price
    kelly_bet = round(max(0, edge * 100), 2)
    
    # Randomly flag a Ghost Trap
    ghost_trap = random.choice([True, False, False, False]) 
    
    return market_id, kalshi_price, model_prob, kelly_bet, ghost_trap

def mock_kalshi_resolution_fetch(market_id):
    """Mocks checking the Kalshi API for expired market resolutions."""
    # 50% chance the market is settled for the mock
    if random.choice([True, False]):
        outcome = random.choice(["YES", "NO"])
        profit = round(random.uniform(-50.0, 50.0), 2)
        return {"status": "settled", "outcome": outcome, "profit_loss": profit}
    return {"status": "active"}

def run_hourly_scan():
    """Pulls Truth Layer, generates Alpha, logs to DB."""
    print(f"\n[{datetime.datetime.now()}] Starting Hourly Weather Scan...")
    
    observations = []
    
    for station in TARGET_STATIONS:
        data = fetch_nws_data(station)
        if data:
            observations.append(data)
            
    if not observations:
        print("No observations fetched. Skipping hourly scan.")
        return
        
    # Generate the On-Chain Root
    merkle_root = generate_merkle_root(observations)
    print(f"Generated Merkle Root: {merkle_root}")
    
    # Log Observations and Predictions
    for obs in observations:
        # 1. Log Truth
        logger.log_observation(obs['city'], obs['temp'], obs['precip'], obs['wind'], merkle_root)
        
        # 2. Log Alpha
        m_id, k_price, m_prob, kelly, ghost = mock_shroomy_engine(obs)
        pred_id = logger.log_prediction(m_id, k_price, m_prob, kelly, ghost)
        print(f"Logged Prediction for {obs['city']} - Market: {m_id} (ID: {pred_id})")

def run_daily_resolution_sweeper():
    """Backtracks database to find missing resolutions and updates them."""
    print(f"\n[{datetime.datetime.now()}] Starting Daily Resolution Sweeper...")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Find markets we predicted that don't have a resolution yet
    cursor.execute("""
        SELECT DISTINCT p.market_id 
        FROM predictions p 
        LEFT JOIN resolutions r ON p.market_id = r.market_id 
        WHERE r.market_id IS NULL
    """)
    unresolved_markets = cursor.fetchall()
    
    print(f"Found {len(unresolved_markets)} unresolved markets in DB.")
    
    resolved_count = 0
    for (market_id,) in unresolved_markets:
        kalshi_data = mock_kalshi_resolution_fetch(market_id)
        
        if kalshi_data["status"] == "settled":
            logger.log_resolution(market_id, kalshi_data["outcome"], kalshi_data["profit_loss"])
            resolved_count += 1
            
    conn.close()
    print(f"Sweep complete. Successfully resolved {resolved_count} markets.")

if __name__ == "__main__":
    print("🚀 Starting Weather Oracle Worker...")
    
    # Run once immediately for testing
    run_hourly_scan()
    run_daily_resolution_sweeper()
    
    print("\nWorker is now active. Entering continuous 1-hour loop...")
    
    # The actual execution loop
    last_sweep_day = datetime.datetime.now().day
    
    while True:
        # Sleep for 1 hour
        time.sleep(3600)
        
        # Hourly tasks
        run_hourly_scan()
        
        # Daily tasks (Run sweeper if the day has changed)
        current_day = datetime.datetime.now().day
        if current_day != last_sweep_day:
            run_daily_resolution_sweeper()
            last_sweep_day = current_day
