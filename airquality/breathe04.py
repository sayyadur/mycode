#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""
# imports always go at the top of your code
import requests

air_now_site = "https://www.airnowapi.org/aq/forecast/zipCode/?"
output_format = "application/json"
zipcode = 20001
date = "2019-07-16"
distance = 25
api_key = "E63862C4-C96B-4795-A454-215A5D5CD905"

LOOKUPAPI = 'https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=95035&date=2019-07-16&distance=25&API_KEY=E63862C4-C96B-4795-A454-215A5D5CD905'
## LOOKUPAPI = air_now_site,'format',output_format,'&zipcode=',zipcode,'&date=',date,'&distance=',distance,'&API_KEY=',api_key

print(LOOKUPAPI)

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get(LOOKUPAPI)

    ## set up screen
    print("Weather Forecast")
    print("----------------")

    # display the JSON we were returned as Pythonic datastructures
# loop across the list returned to us
    for x in r.json():
        print(x.get("DateForecast"))
        print("----------")
        print(x.get("Discussion"))

main()
