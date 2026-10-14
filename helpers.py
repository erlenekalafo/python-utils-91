import time
from typing import Dict, List, Any, Union

def normalize_candle_data(
    raw_candles: List[Union[List[Any], Dict[str, Any]]]
) -> List[Dict[str, Union[int, float]]]:
    """
    Normalizes raw OHLCV candle data from various crypto exchange formats
    into a standard dictionary structure sorted by timestamp.
    """
    normalized = []
    
    for c in raw_candles:
        if isinstance(c, (list, tuple)) and len(c) >= 6:
            # Common standard array format: [timestamp, open, high, low, close, volume]
            normalized.append({
                "timestamp": int(c[0]),
                "open": float(c[1]),
                "high": float(c[2]),
                "low": float(c[3]),
                "close": float(c[4]),
                "volume": float(c[5])
            })
        elif isinstance(c, dict):
            # Key mapping handling standard REST/WebSocket payload variants
            ts = c.get("timestamp") or c.get("t") or c.get("time") or int(time.time() * 1000)
            op = c.get("open") or c.get("o") or 0.0
            hi = c.get("high") or c.get("h") or 0.0
            lo = c.get("low") or c.get("l") or 0.0
            cl = c.get("close") or c.get("c") or 0.0
            vol = c.get("volume") or c.get("v") or 0.0
            
            normalized.append({
                "timestamp": int(ts),
                "open": float(op),
                "high": float(hi),
                "low": float(lo),
                "close": float(cl),
                "volume": float(vol)
            })
            
    return sorted(normalized, key=lambda x: x["timestamp"])


def calculate_vwap(candles: List[Dict[str, Union[int, float]]]) -> float:
    """
    Calculates the Volume Weighted Average Price (VWAP) from normalized candle data.
    """
    if not candles:
        return 0.0

    total_volume = 0.0
    price_volume = 0.0

    for candle in candles:
        # Typical price calculation: (High + Low + Close) / 3
        typical_price = (candle["high"] + candle["low"] + candle["close"]) / 3.0
        volume = float(candle["volume"])

        price_volume += typical_price * volume
        total_volume += volume

    if total_volume == 0.0:
        return 0.0

    return round(price_volume / total_volume, 8)
