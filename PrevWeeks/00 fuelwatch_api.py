import feedparser
import requests
from pprint import pprint

response = requests.get('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Canning Vale', headers={'user-agent': ''})
feed1 = feedparser.parse(response.content)

tommorow = requests.get('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=4&Suburb=Canning Vale&Day=tomorrow', headers={'user-agent': ''})
feed2 = feedparser.parse(tommorow.content)


list = []
for station in feed1["entries"]:

    Dict = {"location": station["location"],
            "address": station["address"],
            "brand": station["brand"],
            "price": station["price"],
            "date": "today"
            }
    list.append(Dict)

for station in feed2["entries"]:

    Dict = {"location": station["location"],
            "address": station["address"],
            "brand": station["brand"],
            "price": station["price"],
            "date": "tomorrow"
            }
    list.append(Dict)

sorted_list = sorted(list, key=lambda x: x["price"])
pprint(sorted_list)
