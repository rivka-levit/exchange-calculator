"""
Extract currency exchange rate.
"""

import os
from bs4 import BeautifulSoup
import requests

from calculs.currencies import currencies

from dotenv import load_dotenv

load_dotenv()


class RateExtractor:
    """Get rate from API."""

    def __init__(self):
        self.api_key = os.environ.get('API_KEY')
        self.base_url = 'http://api.exchangerate.host/'

    def get_rate(self, from_cur: str, to_cur: str) -> float:
        """Return exchange rate for currency pair."""

        params = {
            'access_key': self.api_key,
            'source': from_cur,
            'currencies': to_cur
        }

        r = requests.get(f'{self.base_url}live', params=params)
        data = r.json()
        # return data

        return self.clean_data(data['quotes'][f'{from_cur}{to_cur}'])

    def get_currencies(self):
        """Return list of available currencies."""

        params = {'access_key': self.api_key}
        r = requests.get(f'{self.base_url}list', params=params)

        return r.json()['currencies']

    @staticmethod
    def clean_data(data: str):
        """Convert the rate to rounded float number."""

        return round(float(data), 2)


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
