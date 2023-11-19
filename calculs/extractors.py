"""
Extract currency exchange rate.
"""

import os
import requests

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

        params = {'access_key': os.environ.get('API_KEY')}
        r = requests.get(f'{self.base_url}list', params=params)

        return r.json()['currencies']

    @staticmethod
    def clean_data(data: str):
        """Convert the rate to rounded float number."""

        return round(float(data), 2)


# if __name__ == '__main__':
#     exr = RateExtractor()
#     print(exr.get_rate('USD', 'ILS'))
#     print(exr.get_currencies().keys())

