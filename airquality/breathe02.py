#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""
# imports always go at the top of your code
import requests

LOOKUPAPI = 'https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=95035&date=2019-07-16&distance=25&API_KEY=E63862C4-C96B-4795-A454-215A5D5CD905'

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get(LOOKUPAPI)

    # display the JSON we were returned as Pythonic datastructures
    print(r.json())

main()
