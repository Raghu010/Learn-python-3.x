

"""Calendar module allows output calendars like the program and provides additional useful functions related to the calendar. Functions and classes defined in Calendar
module use an idealized calendar, the current Gregorian calendar extended indefinitely in both directions. By default, these calendars have Monday as the first day
of the week, and Sunday as the last (the European convention)."""

import calendar  
    
yy = 2020
mm = 3 
print(calendar.month(yy, mm))


#Below are the few calendar functions.
"""1.calendar(year, w, l, c) :- This function displays the year, width of characters, no. of lines per week and column separations."""
import calendar
print(calendar.calendar(2020, 4, 1, 5))

#2.firstweekday()- This function returns the first weekday number.By default Monday (number 0).
print(calendar.firstweekday())

#3.isleap(year)- This function checks whether the passed year is leap or not.
print(calendar.isleap(2020))

#4.leapdays(year1, year2)- This function returns the total number of leap days between year1 and year2.
print(calendar.leapdays(2000, 2020))

"""5.month (year, month, w, l) :- This function prints the month of a specific year mentioned in arguments. It takes 4 arguments, year, month, width of characters and
no. of lines taken by a week."""

print(calendar.month(2020, 3, 3, 1))

#6.monthrange(year, month) :- This function returns two integers, first, the starting day number of week(0 as monday) , second, the number of days in the month.
print(calendar.monthrange(2020, 3))

#7.prcal(year, w, l, c) :- This function also prints the calendar of specific year but there is no need of “print” operation to execute this.
calendar.prcal(2020, 3, 1, 5)

#8.prmonth(year, month, w, l) :- This function also prints the month of specific year but there is no need of “print” operation to execute this.
calendar.prmonth(2020, 3, 3, 1)

#9. setfirstweekday(num) :- This function sets the day start number of week.
print(calendar.setfirstweekday(0))

#10.weekday(year, month, date) :- This function returns the week day number(0 is Monday) of the date specified in its arguments.
print(calendar.weekday(2020, 3, 7))
