from datetime import datetime, timezone
from typing import Dict, List, Any


def calculate_vwap(trades: List[Dict[str, Any]]) -> float:
    """Calculate Volume-Weighted Average Price (VWAP) from trade records."""
    total_volume = 0.0
    total_value = 0.0

    for trade in trades:
        price = float(trade.get("price", 0.0))
        amount = float(trade.get("amount", 0.0))
        total_value += price * amount
        total_volume += amount

    if total_volume == 0.0:
        return 0.0
    return round(total_value / total_volume, 8)


def normalize_trade_data(
    raw_trades: List[Dict[str, Any]], symbol: str
) -> List[Dict[str, Any]]:
    """Normalize heterogeneous exchange trade data into standard structure."""
    normalized = []
    for item in raw_trades:
        ts = item.get("timestamp") or item.get("time") or item.get("T")
        if isinstance(ts, (int, float)):
            if ts > 1e11:
                ts = ts / 1000.0
            dt = datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()
        else:
            dt = datetime.now(timezone.utc).isoformat()

        price = float(item.get("price") or item.get("p") or 0.0)
        amount = float(item.get("amount") or item.get("qty") or item.get("q") or 0.0)
        side = str(item.get("side") or item.get("m") or "unknown").lower()

        normalized.append(
            {
                "symbol": symbol.upper(),
                "price": price,
                "amount": amount,
                "volume_usd": price * amount,
                "side": "buy" if side in ["buy", "true", "b"] else "sell",
                "timestamp": dt,
            }
        )
    return normalized


def aggregate_market_summary(raw_trades: List[Dict[str, Any]], symbol: str) -> Dict[str, Any]:
    """Aggregate standard trade metric summary for a cryptocurrency pair."""
    clean_trades = normalize_trade_data(raw_trades, symbol)
    if not clean_trades:
        return {"symbol": symbol.upper(), "trades_count": 0, "vwap": 0.0, "total_volume": 0.0}

    prices = [t["price"] for t in clean_trades]
    total_vol = sum(t["amount"] for t in clean_trades)
    vwap = calculate_vwap(clean_trades)

    return {
        "symbol": symbol.upper(),
        "trades_count": len(clean_trades),
        "high": max(prices),
        "low": min(prices),
        "vwap": vwap,
        "total_volume": round(total_vol, 6),
        "total_turnover": round(sum(t["volume_usd"] for t in clean_trades), 2),
    }
