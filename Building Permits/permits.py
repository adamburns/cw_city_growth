from datetime import datetime
import requests

BASE_URL_UNITS = 'https://www.census.gov/construction/bps/txt/tb3u'
BASE_URL_VALUE = 'https://www.census.gov/construction/bps/txt/tb3v'
CUR_MONTH = datetime.now().month
CUR_YEAR = datetime.now().year
MIN_YEAR = 2004
MAX_MON = CUR_MONTH - 2

for year in range(MIN_YEAR, CUR_YEAR + 1):
    for month in range(1, 13):
        if year == CUR_YEAR and month > MAX_MON:
            break
        else:
            units_loop = (BASE_URL_UNITS + str(year) + format(month, '02d') + '.txt')
            with requests.get(units_loop) as response:
                print(units_loop)
                with open(units_loop[-14:], 'wb') as output:
                    output.write(response.content)
            value_loop = (BASE_URL_VALUE + str(year) + format(month, '02d') + '.txt')
            with requests.get(value_loop) as response:
                print(value_loop)
                with open(value_loop[-14:], 'wb') as output:
                    output.write(response.content)
