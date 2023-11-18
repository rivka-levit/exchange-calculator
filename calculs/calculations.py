"""
Calculator for currency exchange.
"""

from extractors import RateExtractor


class CurrencyConverter:
    """Calculate the sum in target currency."""

    def __init__(self):
        self.extractor = RateExtractor()

    def convert(self, from_cur: str, to_cur: str, value: float):
        """Convert the sum to the target currency."""

        rate = self.extractor.get_rate(from_cur, to_cur)

        return round((value * rate), 2)
