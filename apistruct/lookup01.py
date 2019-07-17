#!/usr/bin/env python3
import requests

def main():
  mytoken = 'fad05263fba188314c4cca71e9832be4429588edd5f59c1f'
  myapi = "https://fonoapi.freshpixl.com/v1/getlatest"
  mybuiltapi = myapi + "?token=" + mytoken

  ## translate our JSON response to a series of Python lists and dictionaries
  myjson = requests.get(mybuiltapi).json()

  ## Display a list of what inside our JSON
  for x in myjson:
    print(x)

if __name__ == '__main__':
  main()
