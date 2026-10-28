from typing import List, Dict, Tuple, Optional


def calculate_vwap(trades: List[Dict[str, float]]) -> float:
    """Calculate Volume Weighted Average Price (VWAP) from trade data."""
    if not trades:
        return 0.0

    total_volume = 0.0
    weighted_price_sum = 0.0

    for trade in trades:
        price = trade.get("price", 0.0)
        amount = trade.get("amount", 0.0)
        total_volume += amount
        weighted_price_sum += price * amount

    if total_volume == 0.0:
        return 0.0

    return round(weighted_price_sum / total_volume, 8)


def compute_orderbook_metrics(
    bids: List[Tuple[float, float]], asks: List[Tuple[float, float]]
) -> Dict[str, Optional[float]]:
    """Calculate spread, mid-price, and depth imbalance for an order book."""
    if not bids or not asks:
        return {"spread": None, "mid_price": None, "imbalance": None}

    top_bid = bids[0][0]
    top_ask = asks[0][0]

    spread = round(top_ask - top_bid, 8)
    mid_price = round((top_ask + top_bid) / 2.0, 8)

    bid_volume = sum(size for _, size in bids)
    ask_volume = sum(size for _, size in asks)
    total_volume = bid_volume + ask_volume

    imbalance = (
        round((bid_volume - ask_volume) / total_volume, 4)
        if total_volume > 0
        else 0.0
    )

    return {
        "spread": spread,
        "mid_price": mid_price,
        "imbalance": imbalance,
    }
