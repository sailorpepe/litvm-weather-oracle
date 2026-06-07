from logger import AlphaEngineLogger
import sqlite3

def test_logger():
    print("Initializing logger...")
    logger = AlphaEngineLogger()

    print("Testing Observation Logging...")
    logger.log_observation(
        city_code="CHI", 
        temp=72.5, 
        precip=0.0, 
        wind=12.2, 
        merkle_root="0xabc123"
    )

    print("Testing Prediction Logging...")
    pred_id = logger.log_prediction(
        market_id="KALSHI-CHI-RAIN", 
        kalshi_price=0.35, 
        model_prob=0.45, 
        kelly_bet=15.5, 
        is_ghost_trap=False
    )
    print(f"Prediction logged with ID: {pred_id}")

    print("Testing Resolution Logging...")
    logger.log_resolution(
        market_id="KALSHI-CHI-RAIN", 
        resolved_outcome="NO", 
        profit_loss=-15.5
    )

    print("\nAuditing Database records...")
    conn = sqlite3.connect("alpha_engine.sqlite")
    cursor = conn.cursor()

    obs = cursor.execute("SELECT * FROM raw_observations").fetchall()
    print(f"Found {len(obs)} observations.")
    assert len(obs) > 0, "Failed to write observation"

    preds = cursor.execute("SELECT * FROM predictions").fetchall()
    print(f"Found {len(preds)} predictions.")
    assert len(preds) > 0, "Failed to write prediction"

    res = cursor.execute("SELECT * FROM resolutions").fetchall()
    print(f"Found {len(res)} resolutions.")
    assert len(res) > 0, "Failed to write resolution"

    print("\n✅ All logger methods audited and working flawlessly.")

if __name__ == "__main__":
    test_logger()
