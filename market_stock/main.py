import os
import requests


from utils import get_date_from, get_date_to
from dotenv import load_dotenv


load_dotenv()
MARKET_API_KEY = os.getenv("MARKET_API_KEY")


def get_stock_info(exchange=None, stock=None, date_from=get_date_from() , date_to=get_date_to()):
    url = f"https://api.marketstack.com/v1/eod?access_key={MARKET_API_KEY}"

    querystring = {
                    "symbols":stock,
                    "exchange":exchange,
                    "date_from":date_from,
                    "date_to":date_to,
                    "interval":"10min"
                    }
    response = requests.get(url, params=querystring)
    return response.json()


def parse_market_response(market_response):
    stock_values = []
    for data_content in market_response["data"]:
        stock_content_dict = {
                              "symbol": data_content["symbol"],
                              "exchange": data_content["exchange"],
                              "date": data_content["date"],
                              "open": data_content["open"],
                              "high": data_content["high"],
                              "low": data_content["low"],
                              "close": data_content["close"],
                              "volume": data_content["volume"]
                            }
        stock_values.append(stock_content_dict)
    return stock_values



if __name__ == "__main__": 
    market_response = get_stock_info(exchange="XNAS", stock="AAPL", date_from=get_date_from() , date_to=get_date_to())
    stock_values_list = parse_market_response(market_response)
    print(stock_values_list)     




   
