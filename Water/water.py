import requests

START_URL = 'https://waterdata.usgs.gov/'
END_URL = '/nwis/water_use?format=rdb&rdb_compression=value&wu_area=County&wu_year=ALL&wu_county=ALL&wu_category=TP&wu_county_nms=--ALL%2BCounties--&wu_category_nms=Total%2BPopulation'

with open('state.txt') as f:
    states = f.readlines()
states = [x.strip() for x in states]
for state in range(states):
    print(state)
    url = START_URL + state.lower() + END_URL
    with requests.get(url) as response:
        with open(state + '.txt', 'wb') as output:
            output.write(response.content)
