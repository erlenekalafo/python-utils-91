from decimal import Decimal, InvalidOperation, DivisionByZero
from typing import Dict, Any, List


class ProcessingError(Exception):
    """Base exception raised during order processing failure."""
    pass


class OrderBookProcessor:
    """Processes raw crypto order book data with strict validation."""

    def __init__(self, max_depth: int = 100):
        if max_depth <= 0:
            raise ValueError("max_depth must be a positive integer")
        self.max_depth = max_depth

    def calculate_weighted_mid_price(self, payload: Dict[str, Any]) -> Decimal:
        """
        Calculates volume-weighted mid price from order book snapshot.
        Handles malformed payloads, zero quantities, and crossed books.
        """
        if not isinstance(payload, dict):
            raise ProcessingError("Invalid payload format: expected dict")

        bids = payload.get("bids", [])
        asks = payload.get("asks", [])

        if not bids or not asks:
            raise ProcessingError("Order book missing bids or asks")

        try:
            best_bid_price = Decimal(str(bids[0][0]))
            best_bid_qty = Decimal(str(bids[0][1]))
            best_ask_price = Decimal(str(asks[0][0]))
            best_ask_qty = Decimal(str(asks[0][1]))
        except (IndexError, TypeError, InvalidOperation) as err:
            raise ProcessingError(f"Malformed price/quantity entry: {err}") from err

        if best_bid_price <= 0 or best_ask_price <= 0:
            raise ProcessingError("Prices must be strictly positive")
        if best_bid_qty <= 0 or best_ask_qty <= 0:
            raise ProcessingError("Quantities must be strictly positive")
        if best_bid_price >= best_ask_price:
            raise ProcessingError("Crossed order book detected")

        total_qty = best_bid_qty + best_ask_qty
        try:
            weighted_mid = (best_bid_price * best_ask_qty + best_ask_price * best_bid_qty) / total_qty
            return weighted_mid.quantize(Decimal("0.00000001"))
        except (ZeroDivisionError, DivisionByZero) as err:
            raise ProcessingError("Total depth quantity cannot be zero") from err

    def sanitize_order_batch(self, orders: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Filters invalid orders and normalizes trade data."""
        valid_orders = []
        for item in orders:
            try:
                symbol = str(item["symbol"]).upper()
                price = Decimal(str(item["price"]))
                amount = Decimal(str(item["amount"]))
                side = str(item["side"]).lower()

                if side not in ("buy", "sell") or price <= 0 or amount <= 0:
                    continue

                valid_orders.append({
                    "symbol": symbol,
                    "price": price,
                    "amount": amount,
                    "side": side,
                    "total": price * amount
                })
            except (KeyError, InvalidOperation, TypeError):
                continue

        return valid_orders
