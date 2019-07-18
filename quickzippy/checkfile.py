#!/usr/bin/env python3
import os
import zipfile

filename = input("Enter the file name to check whether its zip file or not?: ")
print(zipfile.is_zipfile(filename))

