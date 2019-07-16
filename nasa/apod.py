#!/usr/bin/env python3
#
import urllib.request
import json
import webbrowser
from pprint import pprint as pp # part of the standard libray

## define some constants
NASAAPI = 'https://api.nasa.gov/planetary/apod?' # this is our api to call
MYKEY = 'api_key=Qa6ibtesirCSWgSu6kCK33odwyevgbabXrrs2byc' ## this is our api key

## Pretty Print JSON
def main():
    """run-time code"""
    nasaapiobj = urllib.request.urlopen(NASAAPI + MYKEY) # call the webservice
    nasaread = nasaapiobj.read() # parse the JSON blob returned
    convertedjson = json.loads(nasaread.decode('utf-8')) # convert JSON

    # Show converted JSON
    print(convertedjson) # show convereted JSON without pprint
    input('\nThis is converted JSON. Press ENTER to continue.') # pause for enter

    # Show Pretty Print JSON
    pp(convertedjson) # this is Pretty Print in action
    # pprint.pprint(convertedjson) # if you do a simple import pprint, the result is a long usage
    input('\nThis is pretty printed JSON. Press ENTER to continue.') # pause for ENTER

    # Print the description of the photo we are about to view
    print(convertedjson['explanation']) # display the value for the key explanation
    input('\nPress ENTER to view this photo of the day') # pause for ENTER

    webbrowser.open(convertedjson['hdurl']) # open in the webbrowser

main()
