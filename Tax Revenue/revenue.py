import requests

URL = 'https://www2.census.gov/programs-surveys/qtax/tables/2018/q1t1.xls'
with requests.get(URL) as response:
    with open('revenue.xls', 'wb') as output:
        output.write(response.content)
