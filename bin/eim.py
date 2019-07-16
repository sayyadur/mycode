#!/usr/bin/env python3
import http.client
conn = http.client.HTTPConnection("localhost", 9021)
conn.request('HEAD', '/')
res = conn.getresponse()
print(res.status, res.reason)

conn.request('GET', '/') # this time we'll issue GET
res = conn.getresponse() # res is equal to the response associated wtih conn
print(res.status, res.reason) # print the response status code and reason
page_data = res.read()  # page_data is all of the data associated with res 
print(page_data) # this will proint out all of the data assocaited with res

