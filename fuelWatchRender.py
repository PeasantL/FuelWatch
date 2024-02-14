import feedparser
import requests
import webbrowser
from datetime import date

#set the location
location = "Canning Vale"


#retrieve the relevent data, parse into list & dictionary
response = requests.get(f"http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb={location}", headers={"user-agent": ""})
feed1 = feedparser.parse(response.content)

tommorow = requests.get(f"https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=4&Suburb={location}&Day=tomorrow", headers={"user-agent": ""})
feed2 = feedparser.parse(tommorow.content)


#Restructure releavent information
list = []
for station in feed1["entries"]:
    Dict = {"location": station["location"],
            "address": station["address"],
            "brand": station["brand"],
            "price": station["price"],
            "date": "Today"
            }
    list.append(Dict)

for station in feed2["entries"]:
    Dict = {"location": station["location"],
            "address": station["address"],
            "brand": station["brand"],
            "price": station["price"],
            "date": "Tomorrow"
            }
    list.append(Dict)

sorted_list = sorted(list, key=lambda x: x["price"])


#structure each entry of list into html
my_html_tdst = ""
for item in sorted_list:
    my_html_tdst += f'''
    <tr>
    <td>{item["location"]}</td>
    <td>{item["address"]}</td>
    <td>{item["brand"]}</td>
    <td>{item["price"]}</td>
    <td>{item["date"]}</td>
    </tr>
    '''


#html body
my_html = f'''
<html>
  <head>
    <style>

      h1 {{text-align: center;}}

      table {{
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
      }}

      td, th {{
        border: 1px solid #dddddd;
        text-align: center;
        padding: 8px;
      }}

      tr:nth-child(even) {{
        background-color: #dddddd;
      }}

    </style>
  </head>

  <body>
  <h1>Gas Prices at {location} ({date.today()})</h1>
    <table>
        <tr>
            <th>Location</th>
            <th>Address</th>
            <th>Brand</th>
            <th>Price</th>
            <th>Date</th>
        </tr>
        {my_html_tdst}
    </table>
  </body>
</html>
'''


#render and open the html
f = open(f"render-{date.today()}.html", "w")
f.write(my_html)
f.close()
webbrowser.open(f"render-{date.today()}.html")