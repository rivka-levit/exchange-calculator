"""
Extract currency exchange rate.
"""

# import os
from bs4 import BeautifulSoup
import requests

from calculs.currencies import currencies


class RateScrapeExtractor:
    """Extract exchange rate by scraping."""

    base_url = 'https://www.x-rates.com/calculator/'
    currencies = currencies

    def get_rate(self, in_currency: str, out_currency: str) -> float:
        """Scrape and return exchange rate of a currency pair."""

        params = {
            'from': in_currency,
            'to': out_currency,
            'amount': 1
        }

        content = requests.get(self.base_url, params=params).text
        soup = BeautifulSoup(content, 'html.parser')
        rate = soup.find('span', class_='ccOutputRslt').get_text()

        return self.clean_data(rate)

    def get_currencies(self):
        """Return list of available currencies."""

        return self.currencies

    @staticmethod
    def clean_data(data: str):
        """Convert the rate to rounded float number."""

        return round(float(data[:-4]), 2)
