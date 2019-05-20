from bs4 import BeautifulSoup
from time import sleep
import json
import requests

URL = 'https://www.zillow.com/research/data/'

with requests.get(URL) as response:
    soup = BeautifulSoup(response.text, 'lxml')
    soup = soup.findAll('script')
    soup = soup[len(soup) - 25]
    soup = str(soup).replace('\\', '')
    soup = json.loads(soup[17:-10])
    #Traverse over nested dictionary in the script to get the URLs
    for dataType in soup:
        for x in soup[dataType]:
            for y in soup[dataType][x]:
                temp_url = soup[dataType][x][y]
                with requests.get(temp_url) as csv:
                    #Split the string to get the filename in format X.csv or X.xlsx
                    temp_name = temp_url.split('/')[-1]
                    with open(temp_name, 'wb') as output:
                        print(temp_name)
                        output.write(csv.content)
                        #time out to avoid DDOS
                        sleep(5)
