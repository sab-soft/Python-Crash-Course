# program to display the following 
from datetime import date, timedelta
import time 
import calendar
print("The current date and time is: ", time.ctime())
print("Today date is: ", date.today().strftime("%Y, %B %d"))
print("the time is: ", time.strftime("%H %M %S"))
print("The month of the year: ", date.today().strftime("%B"))
print("The number of week of the year: ", date.today().strftime("%W"))
print("The day of the week is: ", date.today().strftime("%A"))
print("Today is the {} day of the year".format(date.today().strftime("%j")))
print("Today is the {} day of the week".format(date.today().strftime("%w")))
print()

# program to check ffor leap years 
years = [1900, 2016, 1816, 2020, 1454, 2030, 2025, 2027]

index = 0

while index < len(years):

    year = calendar.isleap(years[index])

    if year == True:
        print("The current year {} is a leap year".format(years[index]))
    else: 
        print("The current year {} is not a leap year".format(years[index]))

    index += 1
print()

# A progam to calculate a year from today's date 

current_year = date.today()

one_year = current_year + timedelta(365)

print("Current date: ", current_year)
print("A year from today is: ", one_year)
print()

# print the next seven days from today 
index = 0 
while index < 8:
    
    current_day = date.today() + timedelta(index)
    current_day = current_day.strftime("%A \t %w \t %d")
    index += 1

    print(current_day)

aug = calendar.month(2024, 8)
sept = calendar.month(2024, 9)

print(aug)
print(sept)
