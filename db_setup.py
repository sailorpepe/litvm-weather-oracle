import sqlite3
import os

DB_PATH = "alpha_engine.sqlite"

def setup_database():
    """Initializes the SQLite database with WAL mode and the ML training schema."""
    conn = sqlite3.connect(DB_PATH)
    
    # Enable WAL mode for high concurrency (essential for high-frequency oracles)
    conn.execute("PRAGMA journal_mode=WAL")
    
    cursor = conn.cursor()

    # 1. The Truth Layer (Raw Observations from ASOS/NWS)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS raw_observations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp INTEGER NOT NULL,
            city_code TEXT NOT NULL,
            temperature REAL,
            precipitation_1h REAL,
            wind_speed REAL,
            merkle_root TEXT
        )
    """)
    # Index for fast querying by city and time during ML training
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_obs_time_city ON raw_observations(timestamp, city_code)")

    # 2. The Alpha Layer (Predictions made by the Shroomy Engine)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            prediction_id TEXT PRIMARY KEY,
            timestamp INTEGER NOT NULL,
            market_id TEXT NOT NULL,
            kalshi_current_price REAL NOT NULL,
            model_probability REAL NOT NULL,
            kelly_bet_size REAL NOT NULL,
            ghost_trap_flag BOOLEAN NOT NULL
        )
    """)
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_pred_market ON predictions(market_id)")

    # 3. The Ground Truth (Final Market Resolutions from Kalshi)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resolutions (
            market_id TEXT PRIMARY KEY,
            resolved_outcome TEXT NOT NULL,
            resolution_timestamp INTEGER NOT NULL,
            profit_loss REAL
        )
    """)

    conn.commit()
    conn.close()
    print(f"✅ Successfully initialized {DB_PATH} with WAL mode and ML schema.")

if __name__ == "__main__":
    setup_database()
