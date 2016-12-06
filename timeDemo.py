# Python code to demonstrate the working of
# time() and gmtime()

import time
# using time() to display time since epoch
print("Seconds elapsed since the epoch are : ")
print(time.time())

# using gmtime() to return the time attribute structure
print("Time calculated acc. to given second is : ")
print(time.gmtime())

# Python code to demonstrate the working of
# asctime() and ctime()

ti = time.gmtime()

# using asctime() to display time acc. to time mentioned
print("Time calculated using asctime() is : ")
print(time.asctime(ti))

# using ctime() to display time string using seconds
print("Time calculated using ctime() is : ")
print(time.ctime())

# Python code to demonstrate the working of
# sleep()

print("Start Execution : ")
print(time.ctime())
# using sleep() to halt execution
# time.sleep(4)

# using ctime() to show present time
print("Stop Execution: ")
print(time.ctime())

# Python code to demonstrate the working of
# MINYEAR and MAXYEAR
import datetime
from datetime import date
# using MINYEAR to print minimum representable year
print("Minimum representable year is : ")
print(datetime.MINYEAR)
print("Maximum representable year is : ")
print(datetime.MAXYEAR)

# Python code to demonstrate the working of
# date() and today()
print("The represented date is : ")
print(datetime.date(1997,4,1))

print("Present date is : ")
print(date.today())

# Python code to demonstrate the working of
# fromtimestamp(), min() and max()
print("The calculated date from seconds is : ")
print(date.fromtimestamp(3452435))

print("Minimum representable date is :")
print(date.min)

print("Maximum representable date is : ")
print(date.max)
