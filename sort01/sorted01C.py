#!/usr/bin/env python3

rfile = open("sorted01.py", "r")
wfile = open("sortedoutput.txt", "w")

#print(sorted(zfile.readlines()))
wfile.write(str(sorted(rfile.readlines())))

rfile.close()
wfile.close()
