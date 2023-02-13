from BinanceHandler import get_current_price
from datetime import datetime, timedelta
import time

max_price_last_hour = {"max_price":1.0, "time":datetime.now()}
current_price = 0.0


def compare_the_last_hour(price):
    if price/max_price_last_hour.get('max_price')>=0.01:

        print(f"The price has fallen: {price}")
    else:
        print(f'Fallen by {price/max_price_last_hour.get("max_price")}')



while 1!=0:
    current_price = get_current_price()
    current_time = datetime.now()
    if (current_time-max_price_last_hour['time']).total_seconds()==3600.0:
        max_price_last_hour['max_price']=current_price
        max_price_last_hour['time'] = datetime.now
    elif (current_time-max_price_last_hour['time']).total_seconds()<3600.0:
        if max_price_last_hour['max_price']<current_price:
            print("Price raised!")
            max_price_last_hour['max_price'] = current_price
        else:
            compare_the_last_hour(current_price)
    else:
        print("we are broke")
    time.sleep(5)

