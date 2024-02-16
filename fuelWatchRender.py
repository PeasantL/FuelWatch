import feedparser
import requests
import webbrowser
from datetime import date
from urllib.parse import urlencode


#set the location
location = "Canning Vale"


#parse function from api
def get_fuel(location, tomorrow=False):
    q = urlencode({
        'Product': 1,
        'Suburb': location,
        'Day': 'tomorrow' if tomorrow else 'today'
    })
    response = requests.get(f"http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?{q}", headers={"user-agent": ""})
    feed = feedparser.parse(response.content)

    return [
        {
            "location": station["location"],
            "address": station["address"],
            "brand": station["brand"],
            "price": station["price"],
            "date": "Tomorrow" if tomorrow else "Today",
        }
        for station in feed["entries"]
    ]


feed1 = get_fuel(location)
feed2 = get_fuel(location, tomorrow=True)
sorted_list = sorted(feed1 + feed2, key=lambda x: x["price"])


#structure each entry of list into html
my_html_tdst = ''.join(
    f'''
    <tr>
    <td>{item["location"]}</td>
    <td>{item["address"]}</td>
    <td>{item["brand"]}</td>
    <td>{item["price"]}</td>
    <td>{item["date"]}</td>
    </tr>
    '''
    for item in sorted_list)


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
with open(f"render-{date.today()}.html", "w") as f:
    f.write(my_html)
 
webbrowser.open(f"render-{date.today()}.html")