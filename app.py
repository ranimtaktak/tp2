# This example uses Python 2.7 and the python-request library.

from requests import request,Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from dotenv import load_dotenv
import os
#!!!

def configure():
    load_dotenv()
    
def extract_price(response):
    data = json.loads(response.text)
    return data["data"][0]["quote"]["USD"]["price"]


CRYPTO = "BTC"
URL = "https://pro-api.coinmarketcap.com/v2/tools/price-conversion"
PARAMETERS = {"amount": 1, "symbol": CRYPTO}
HEADERS = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": os.getenv('api_key'),
}

session = Session()
session.headers.update(HEADERS)
try:
    response = session.get(URL, params=PARAMETERS)
    price = extract_price(response)
    print(f'The price of {CRYPTO} is {price} USD')
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
