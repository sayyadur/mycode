#!/usr/bin/env python3
import time # This is required to include time module

## Count the number of ticks from the epoch
ticks = time.time()
print(f"Number of ticks since 12:00am, January 1, 1970: {ticks}")

## Show how we can convert ticks into a useful time tuple
myTime = time.localtime(ticks) # pass ticks to localtime
print(f"The local time tuple is: {myTime}")
print(f"The local time tuple year is: {myTime[0]}")
print(f"The local time tuple month is: {myTime[1]}")
print(f"The local time tuple day is: {myTime[2]}")
print(f"The local time tuple hour is: {myTime[3]}")
print(f"The local time tuple minute is: {myTime[4]}")
print(f"The local time tuple second is: {myTime[5]}")
print(f"The local time tuple week is: {myTime[6]}")
print(f"The local time tuple year is: {myTime[7]}")
print(f"The local time tuple daylight savings is: {myTime[8]}")    

for x in range(10,0,-1):
  print(f'This program will end in..., {x}')
  time.sleep(5)
