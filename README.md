# City Growth 

## Introduction 

City growth can be attributed to many things, and infrastructure development is a heavy indicator of such activity. Building Permit, and Water usage data were included to proxy infrastructure growth. In a similar light, the economic growth can be modelled using Employment, Housing Value, School Enrollment. General city growth may be attributed to the classic Population increase, although this type of growth alone doesn’t imply successful growth. Lastly, airline data may also be a good indicator of a city’s growth as proxied by demand as a destination city (although this may be due to tourism). 

## Requirements 

All data in this directory was obtained using either Python scripts or `wget` from Linux’s command line. The following libraries will be needed for the scripts to function:  
* BeautifulSoup4 
* json 
* requests 
* time 

## To do 
Given more time, I would gather more data on infrastructure usage/spending over metropolitan cities (electricity, oil/gas, sewage). I would also want to know how much a city spends on their roads and the average commute time of its citizens. Another avenue to take is to use the [urbansprawl package](https://github.com/lgervasoni/urbansprawl) to quantify the physical expansion of cities into surrounding areas. 

Technologically, I would like to expand on the Flight data scraping mechanism to get data all the way back to 2004 manipulating the body of a POST request. 

## Metadata
### Building Permits 
Obtained from the [Census Bureau’s Building Permits Survey](https://www.census.gov/construction/bps/) using the `permits.py` script. Building permit data was downloaded by value of property (tb3vXXXXYY.txt), and by number of units approved (tb3uXXXXYY), where XXXX is the year and YY is the month. The text files can be parsed using Python’s stripping functionality. 

Time range: 2004-01 – 2019-03 
### Employment 
Obtained from the [Bureau of Labor Statistics](https://www.bls.gov/) using `wget` on Linux. This data set quantifies the Civilian Workforce, Employed, Unemployed, Unemployment Rate by major Metropolitan areas on a monthly-basis. The data is stored in a text file, which can later be parsed with Python’s stripping functionality for processing in a data frame. 

Time range: 1990-01 – 2019-03 
### Flights 
Flight data was scraped from the [Bureau of Transportation Statistics database](https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236) using `wget`. The data describes the monthly routes taken by airlines on a monthly basis. File type: CSV 
### Housing Values 
Data acquired from [Zillow](http://zillow.com/research/data) on 2019-05-20 using the `values.py` Python script. Aggregated data on this page is made freely available by Zillow for non-commercial use. The data is stored in either csv or xlsx files, easily parsable formats. 

Time range: 2010-01 – 2019-04 
### Population 
Obtained from the [Census Bureau](https://www.census.gov/programs-surveys/popest/data/data-sets.html) using `wget`. This data set quantifies the population over metropolitan areas annually over an 8-year period (2010-2018). The data is in the csv format, which can easily be parsed into manipulatable data. 
### School 
Obtained from the [National Center for Education Statistics](https://nces.ed.gov/programs/digest/d17/) using the `school.py` script. The data shows school enrollment statistics from 1990 and projects figures until 2027 by State and Geographic region. 
### Water 
Obtained from the [U.S. Geological Survey](https://waterdata.usgs.gov/nwis) using the `water.py` script. The data shows water usage statistics at a county-level from 1985 to 2015, every 5 years. The data is stored in text files, which can be parsed with Python’s strip function. 
