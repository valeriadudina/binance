import requests
import json
def get_current_price():
    url = "https://api.binance.com/api/v3/avgPrice?symbol=XRPUSDT"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    return float(json.loads(response.text).get('price'))

