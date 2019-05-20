import requests

URL = 'http://files.zillowstatic.com/research/public/City/City_Zhvi_AllHomes.csv'

with requests.get(URL) as response:
    with open('City_Zhvi_AllHomes.csv', 'wb') as output:
        output.write(response.content)


