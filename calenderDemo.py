# Python code to demonstrate the working of
# calendar() and firstweeksday()

import calendar

# using calendar to print calendar of year
# prints calendar of 2012
print("The calendar of 2012 is : ")
print(calendar.calendar(2012,2,1,6))

# using firstweeksday() to print starting day number
print("The starting day number in calendar is : ")
print(calendar.firstweekday())

# Python code to demonstrate the working of
# isleap() and leapdays()

# using isleap() to check if year is leap or not
if (calendar.isleap(2008)):
    print("The year is leap")
else:
    print("The year is not leap")

# using leapdays() to print leap days between years
print("The leap days between 1950 and 2000 are : ")
print(calendar.leapdays(1950, 2000))

# Python code to demonstrate the working of
# month()

# using month() to display month of specific year
print("The month 5th of 2016 is : ")
print(calendar.month(2016, 5, 2, 1))

# Python code to demonstrate the working of
# monthrange() and prcal()
# using monthrange() to print start week day and
# number of month
print("The start week number and no. of days of month : ")
print(calendar.monthrange(2008, 2))

# using prcal() to print calendar of 1997
print("The calendar of 1997 is : ")
calendar.prcal(1997, 2,1,5)

# Python code to demonstrate the working of
# prmonth() and setfirstweekday()

# using prmonth() to print calendar of 1997
print("The 4th month of 1997 is : ")
calendar.prmonth(1997, 4, 2, 1)

# using setfirstweekday() to set first week day number
calendar.setfirstweekday(4)

# using firstweeksday() to check the changed day
print("The new week day number is : ")
print(calendar.firstweekday())

# using weekday() to print any number of date
print("The day number of 25 Apirl 1997 is ")
print(calendar.weekday(1997, 4, 25))
