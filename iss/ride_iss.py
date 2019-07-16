#!/usr/bin/env python3
import urllib.request
import json
## Trace the ISS
majortom = 'http://api.open-notify.org/astros.json'

## Call the webservice
groundctrl = urllib.request.urlopen(majortom)

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
