import time

time.time()
print(time.time())

print(time.asctime(time.localtime((time.time())))) 
print()

print(time.asctime(time.localtime(time.time())))
print()

print(time.ctime())
print()

# Datetime module 
import datetime

print("current date and time", datetime.datetime.now())
print("Current year", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month: ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))
print()

# Calendar module 
import calendar

# print a calendar for a given month (2024, May)
# calender(year, month)
cal = calendar.month(2032, 2)
print("Here is the calendar: ")
print(cal)

# check for leap year 
# returns true if year is a leap year; otherwise, false 
# calender.isleap(year)
print(calendar.isleap(2024))

# returns the total number of leap days in the years within range(y1, y2)
# calender.leapdays(startyear, endyear)
print(calendar.leapdays(2000, 2024))


# returns a multiline string with a calendar for month month of year year, one line per week
# plus two header lines. w is the width iin characters of each date; 
# each line has length 7*w+6. 1 is the number o lines ffor each week 
# calendar.month(year, month, w=2, 1=1)
print(calendar.month(2024, 5, w=10, l=1))

# returns the weekday code for the given date. Weekday codes are 0 (Monday) to 6 (Sunday); 
# month numbers are 1 (January) to 12 (December)
# calender(year, month, day)
print(calendar.weekday(2024, 5, 4))

# returns a multiline string with a calendar for year year formatted into three columns separted by c spaces. 
# w is the width in characters of each date; each line has length 21*w+18+2*c. l is the number of lines for each week. 
print(calendar.calendar(2024, w=2, l=1, c=5))

# returns the current setting for the weekday that starts each week. By default, when calender is first import, 
# this is 0, meaning Monday
print(calendar.firstweekday())

# sets the first day of each week to weekday code weekday. weekday codes are 0 (Monday) to 6 (Sunday)
# calender.setfirstweekday(weekday) 
print(calendar.setfirstweekday(3))
print(calendar.firstweekday())

# returns the weekday code for the given date 
# calender.weekday(year, month, day)
print(calendar.weekday(2024, 5, 4))
print()

# Date Mathematics 


# calculate one year from today
from datetime import date, timedelta

today1 = date.today()

dt = today1 + timedelta(31)


print("Todays date is: ", today1)
print("One year from today will be: ", dt)
print()

# calculate how many days past new yearr 
dt = date.today()

ny = date(dt.year, 1, 1)

if ny<dt:
    print("Todays date is: ", dt)
    print("It's {0:}".format((dt-ny).days), 'days past new year')
    print()

# other python datetime modeul 
# pytz module 
# dateutil module 


# Application 

# A program to print month calender and year for user input 
'''
mon = int(input("Please enter any month of the year from (1-12): "))
year = int(input("Please enter any year in four digit: "))
print()

month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

print('Month of {} {}'.format(month[mon-1], year))
print()

print('++++++++++++++++++++++++++++++++++++++++++++++++')
print()

print(calendar.month(year, mon))
print()
'''

# A program to calculate age from current and user's yea of birth 
'''
user_year = int(input("Enter the year of your birth in four digit: "))
print()

current_year = date.today().strftime("%Y")

age = int(current_year) - user_year

print("Your year of birth is: ", user_year)
print()
print("Current year is: ", current_year)
print()
print("Your age is: ",age)
'''

# A program to check if a user is eligible for employmentn if he/she is less than 30 years 
user_year = int(input("Enter the year of your birth: "))

current_year = date.today().strftime("%Y")

age = int(current_year) - user_year

if (age < 30): 
    print("Congratulation you are eligible for this job offer!")
    print("Your age is: ", age)

else:
    print("Sorry, you are not eligible for this job offer!")