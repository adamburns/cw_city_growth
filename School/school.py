import requests

URL = 'https://nces.ed.gov/programs/digest/d17/tables/xls/tabn203.20.xls'

with requests.get(URL) as response:
    with open('school.xls', 'wb') as output:
        output.write(response.content)
