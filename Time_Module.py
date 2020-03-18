#Time functions in python.

"""Python has defined a module named time which deals with the operations related to time, its conversions and representations. The beginning of time is measured
starting from 1 january, 12:00am, 1970 and this very time is reffered to as epoch in python"""

#1.time()- This function is used to count the number of seconds elapsed since the epoch.
import time
print(time.time())

"""2.gmtime(sec)- This function returns a structure with 9 values each representing a time attribute in sequence. It converts seconds into time attributes(days, years,
months etc.) till specified seconds from epoch. If no seconds are mentioned, time is calculated till present."""

import time
print(time.gmtime())

import time
print(time.gmtime(1583986486.938189))

#3.asctime('time')- This function takes a time attributed string produced by gmtime() and returns a 24 character string denoting time.

import time
ti = time.gmtime()
print(time.asctime(ti))

"""#4.ctime(sec)- This function returns a 24 character time string but takes seconds as argument and computes time till mentioned seconds. If no argument is passed,
time is calculated till present."""

import time
print(time.ctime())

#5. sleep(sec) :- This method is used to hault the program execution for the time specified in the arguments.

import time
print(time.ctime())

#time.sleep(5)

print(time.ctime())

#Date Manipulations: Date manipulation can also be performed using Python using “datetime” module and using “date” class in it.

#1.MINYEAR- It displays the minimum year that can represented using date class.
import datetime
from datetime import date
print(datetime.MINYEAR)

#2.MAXYEAR- It displays the maximum year that can be represented using date class.
import datetime
from datetime import date
print(datetime.MAXYEAR)

#3.date(yyyy, mm, dd) - This function returns a string with passed arguments in order of year, months and date.
import datetime
from datetime import date
print(datetime.date(2020, 3, 12))

#4.today()- Returns the date of present day in the format yyyy-mm-dd.
import datetime
from datetime import date
print(date.today())

#5.fromtimestamp(sec)-  It returns the date calculated from the seconds elapsed since epoch mentioned in arguments.
import datetime
from datetime import date
import time
print(time.time())
print(date.fromtimestamp(1583989349.4221003))

#6.min()- This returns the minimum date that can be represented by date class.
from datetime import date
print(date.min)

#7.max()- This returns the maximum date that can be represented by date class.
print(date.max)
