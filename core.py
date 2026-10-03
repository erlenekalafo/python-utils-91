from typing import Dict, List, Optional, Tuple


class OrderBookAggregator:
    """Optimized order book depth aggregator and VWAP calculator for streaming market data."""

    def __init__(self, depth_limit: int = 50):
        self.depth_limit = depth_limit
        self._bids: Dict[float, float] = {}
        self._asks: Dict[float, float] = {}
        self._vwap_cache: Optional[Tuple[float, float]] = None

    def update_levels(self, bids: List[Tuple[float, float]], asks: List[Tuple[float, float]]) -> None:
        """Batch update bid and ask price levels with cache invalidation."""
        for price, size in bids:
            if size == 0:
                self._bids.pop(price, None)
            else:
                self._bids[price] = size

        for price, size in asks:
            if size == 0:
                self._asks.pop(price, None)
            else:
                self._asks[price] = size

        self._vwap_cache = None

    def get_top_depth(self) -> Dict[str, List[Tuple[float, float]]]:
        """Returns sorted top bids and asks up to configured depth limit."""
        sorted_bids = sorted(self._bids.items(), reverse=True)[:self.depth_limit]
        sorted_asks = sorted(self._asks.items())[:self.depth_limit]
        return {"bids": sorted_bids, "asks": sorted_asks}

    def calculate_vwap(self) -> Tuple[float, float]:
        """Fast calculation of bid and ask VWAP using memoized state."""
        if self._vwap_cache is not None:
            return self._vwap_cache

        def _compute_side_vwap(levels: Dict[float, float]) -> float:
            total_volume = sum(levels.values())
            if total_volume == 0:
                return 0.0
            total_value = sum(p * v for p, v in levels.items())
            return total_value / total_volume

        bid_vwap = _compute_side_vwap(self._bids)
        ask_vwap = _compute_side_vwap(self._asks)
        self._vwap_cache = (bid_vwap, ask_vwap)
        return self._vwap_cache
