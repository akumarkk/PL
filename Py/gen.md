###### datetime
epoch jan 1st 1970
ctime() time
datetime() datetime


import time
time.time() # epoch seconds
time.ctime(epochseconds) # datetime

- datetime
import datatime as dt
dt.datetime.today()
dt.datetime.today().day/month/year/hour/minute/second

d = date(2018, 12, 1)
t = time(23,45)
dt = datetime.combine(d, t)
dt.datetime.now()/utcnow()

- sorting datetime
    lstdates.append(date(2016, 8, 12))
    lstdates.append(date(2017, 8, 12))
    lstdates.append(date(2018, 8, 12))
    lstdates.sort()

###### sleep
 - import time; time.sleep(seconds)
 - 

###### perf_counter
    start = time.perf_counter() #time in seconds
    end = time.perf_counter()

##### Top-Level Components in Python: A Comprehensive Guide

In Python, top-level components refer to code that is executed directly when a script is run, outside of any functions, classes, or other indented blocks. These components define the main logic and behavior of the program.
