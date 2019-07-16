#!/usr/bin/env python3  
"""Alta3 Research || Author: RZFeeser@alta3.com"""

import urllib.request
import json

## Trace the ISS
## this is now a global and should be capitalized
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    ## Call the webservice
    groundctrl = urllib.request.urlopen(MAJORTOM)

    ## put fileobject into helmet
    helmet = groundctrl.read()

    ## decode JSON to Python data structure
    helmetson = json.loads(helmet.decode('utf-8'))

    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(helmetson)

    print("\n\nPeople in Space: ", helmetson['number'])
    people = helmetson['people']
    print(people)

main()    
