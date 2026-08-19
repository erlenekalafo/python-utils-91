from typing import Dict, Any, Union

class CryptoAnalyzer:
    """Class for analyzing cryptocurrency data."""

    def __init__(self, data: Dict[str, Union[int, float]]) -> None:
        """Initializes the CryptoAnalyzer with data.

        Args:
            data (Dict[str, Union[int, float]]): A dictionary containing cryptocurrency metrics.
        """
        self.data = data

    def calculate_market_cap(self) -> float:
        """Calculates the market capitalization.

        Returns:
            float: The calculated market cap.
        """
        return self.data.get('price', 0) * self.data.get('supply', 0)

    def calculate_volatility(self) -> float:
        """Calculates the volatility of the cryptocurrency.

        Returns:
            float: The calculated volatility.
        """
        price_changes = self.data.get('price_changes', [])
        avg_change = sum(price_changes) / len(price_changes) if price_changes else 0
        return avg_change

    def get_summary(self) -> Dict[str, Any]:
        """Returns a summary of the cryptocurrency analysis.

        Returns:
            Dict[str, Any]: A dictionary summary containing key metrics.
        """
        return {
            'market_cap': self.calculate_market_cap(),
            'volatility': self.calculate_volatility()
        }
