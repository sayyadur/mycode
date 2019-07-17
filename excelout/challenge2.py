#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

LOOKUPAPI = 'http://api.open-notify.org/astros.json' #Replace me with AirNows Generated URL

# imports always go at the top of your code
import requests, json, pyexcel

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get(LOOKUPAPI)
    print(type(r))

    # display the methods available to our new object
    json_struct = r.json()
    print(type(json_struct))
    print(json_struct)

    # helmetson = json.loads(helmet.decode('utf-8'))
    pyexcel.save_as(records=json_struct['people'], dest_file_name="iss_names.xls")

main()
