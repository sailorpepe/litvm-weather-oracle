import sqlite3
import time
import uuid
import json

class AlphaEngineLogger:
    """
    Handles logging of observations, predictions, and resolutions to the SQLite DB.
    This creates the historical dataset needed to train future ML models.
    """
    def __init__(self, db_path="alpha_engine.sqlite"):
        self.db_path = db_path

    def _get_connection(self):
        # Timeout helps handle concurrent writes when WAL mode is active
        return sqlite3.connect(self.db_path, timeout=10.0)

    def log_observation(self, city_code: str, temp: float, precip: float, wind: float, merkle_root: str):
        """Logs the raw NWS/ASOS data (The Truth Layer)."""
        timestamp = int(time.time())
        with self._get_connection() as conn:
            conn.execute("""
                INSERT INTO raw_observations (timestamp, city_code, temperature, precipitation_1h, wind_speed, merkle_root)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (timestamp, city_code, temp, precip, wind, merkle_root))
            conn.commit()

    def log_prediction(self, market_id: str, kalshi_price: float, model_prob: float, kelly_bet: float, is_ghost_trap: bool) -> str:
        """Logs what the Shroomy Engine decided to do (The Alpha Layer)."""
        pred_id = str(uuid.uuid4())
        timestamp = int(time.time())
        with self._get_connection() as conn:
            conn.execute("""
                INSERT INTO predictions (prediction_id, timestamp, market_id, kalshi_current_price, model_probability, kelly_bet_size, ghost_trap_flag)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (pred_id, timestamp, market_id, kalshi_price, model_prob, kelly_bet, is_ghost_trap))
            conn.commit()
        return pred_id

    def log_resolution(self, market_id: str, resolved_outcome: str, profit_loss: float = 0.0):
        """Logs the actual outcome from Kalshi (The Ground Truth)."""
        timestamp = int(time.time())
        with self._get_connection() as conn:
            # We use INSERT OR REPLACE so if we check the resolution twice, we just update it
            conn.execute("""
                INSERT OR REPLACE INTO resolutions (market_id, resolved_outcome, resolution_timestamp, profit_loss)
                VALUES (?, ?, ?, ?)
            """, (market_id, resolved_outcome, timestamp, profit_loss))
            conn.commit()
