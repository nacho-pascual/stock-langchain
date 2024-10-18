

import requests


from utils import get_date_from, get_date_to


def get_stock_info(exchange, stock, date_from=get_date_from() , date_to=get_date_to()):



url = "https://api.marketstack.com/v1/eod?access_key={PASTE_YOUR_API_KEY_HERE}"

querystring = {"symbols":"AAPL"}

response = requests.get(url, params=querystring)

print(response.json())

if __name__ == "__main__": 