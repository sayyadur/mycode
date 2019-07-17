#!/usr/bin/env python3

## python3 -m pip install --user pyexcel
## python3 -m pip install --user pyexcel-xls

import pyexcel

## What is the name of the xls file?
varfilename = input('What is the name of the file? Do not include extension ')

myexcelval = { }

varfilename = varfilename + ".xls"

## Dump Excel spreadsheet to a record format friendly to python
excelrecords = pyexcel.iget_records(file_name=varfilename)

for x in excelrecords:
  totalsocket = x['ip'] + ":" + str(x['port'])
  myexcelval.update ( { x['service'] : totalsocket } ) ## adds a new
                   ## IP and driver key:value pair to our dictionary
print(myexcelval)
