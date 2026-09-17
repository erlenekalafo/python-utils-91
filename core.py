from typing import List, Dict, Tuple, Any


def calculate_vwap(trades: List[Dict[str, float]]) -> float:
    """
    Calculate Volume-Weighted Average Price (VWAP) from a list of trades.
    Each trade dictionary must contain 'price' and 'volume'.
    """
    if not trades:
        return 0.0

    total_volume = sum(trade.get("volume", 0.0) for trade in trades)
    if total_volume == 0.0:
        return 0.0

    price_volume_sum = sum(trade.get("price", 0.0) * trade.get("volume", 0.0) for trade in trades)
    return round(price_volume_sum / total_volume, 8)


def calculate_orderbook_imbalance(bids: List[Tuple[float, float]], asks: List[Tuple[float, float]], depth: int = 10) -> float:
    """
    Calculate bid-ask orderbook volume imbalance for a specified depth level.
    Returns a value between -1.0 (sell pressure) and 1.0 (buy pressure).
    """
    top_bids = bids[:depth]
    top_asks = asks[:depth]

    bid_vol = sum(size for _, size in top_bids)
    ask_vol = sum(size for _, size in top_asks)

    total_vol = bid_vol + ask_vol
    if total_vol == 0.0:
        return 0.0

    return round((bid_vol - ask_vol) / total_vol, 4)


def normalize_ohlcv_series(raw_candles: List[List[Any]]) -> List[Dict[str, float]]:
    """
    Parse standard raw exchange OHLCV arrays into structured dictionaries.
    Expected format per candle: [timestamp, open, high, low, close, volume]
    """
    formatted_candles = []
    for candle in raw_candles:
        if len(candle) < 6:
            continue
        formatted_candles.append({
            "timestamp": float(candle[0]),
            "open": float(candle[1]),
            "high": float(candle[2]),
            "low": float(candle[3]),
            "close": float(candle[4]),
            "volume": float(candle[5])
        })
    return formatted_candles
