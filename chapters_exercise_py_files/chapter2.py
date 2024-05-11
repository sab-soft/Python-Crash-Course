# Data Types 
# Tuples, Range, Set and Dictionary 

# Tuples 
# A tuples is a collection which is ordered and unchangeable. In python tuples are written with round brackets. 

'''
# Creating a tuple 
hobby = ('singing', 'reading', 'designing')
print(hobby)
print(type(hobby))

# Create a one tuple; NOTE don't forget the comma 
chores = ('piano playing',)
print(chores)

# Index a tuple 
best_hobby = hobby[0]
print(best_hobby)

# Change the value of an item in a tuple
# Note: you cannot directly change an item in a tuple 
# You have to convert it to a list first before you can change 

change_hobby = list(hobby)
change_hobby[1] = 'coding'
hobby = tuple(change_hobby)
print(hobby)
'''

# Adding item to a tuple 
# Once a tuple is created, you cannot add items to it. 
# Tuples are unchangeable 
# Items cannot be removed neither

'''
hobby = ('singing', 'coding', 'designing')
hobby[3] = 'reading'
print(hobby) # This will raise a TypeError 
'''

# joining two tuples 
'''
hobby = ('singing', 'coding', 'designing')
years = (24, 25, 52)
hobby_year = hobby + years 
print(hobby_year)
'''

# Trying changing of item in a tuple again 
'''
hobby = ('singing', 'coding', 'designing')
change_hobby = list(hobby)
change_hobby[2] = 'reading'
hobby = tuple(change_hobby)
print(hobby)
'''

# Range 
# Most commonly used when using a for loop 
# find all x such that a <= x < b
# Range can be called with 1, 2, or 3 parameter 
# where 1=an integer equating to 0 to 1
# 2 two integer delimiting start and finish of range 
# 1, 2, 3 i.e start, finish, and step
'''
figure = range(10)
print(type(figure))
print()

print(figure)

new_figure = list(figure)
print(new_figure)

numbers = range(2, 20, 2)
list_of_numbers = list(numbers)
print(list_of_numbers)
'''

# Set 
# Sets are collections which contain all unique elements of a collection. 
# Similar to frozensets which is immutable 
# A set can be said to be a unique list while 
# A frozenset can be said to be a unique tuple 
# A set has the following functions * add * difference * intersection * remove * len * union 
# Given that x and y are set variables
# add x.add(element)
# difference x.difference(y)
# intersection x.intersection(y)
# remove x.remove(element)
# union x.union(y)

'''
list_of_friends = ['Friend', 'Phirell', 'John', 'Festus', 'Joseph', 'Friend', 'Larai']
family = ['Amakundi', 'Fosen', 'Mother', 'Father', 'Tubasen', 'Larai']

set1 = set(list_of_friends)
set2 = set(family)

# print(set1, set2)

print()

set1.add('Bob')
set2.add('Miracle')

# diff = set1.difference(set2)

# similar_names = set1.intersection(set2)

# delete_item = set1.remove('Phirell')

# no_of_friends = len(set1)

family_n_friends = set1.union(set2)

print(family_n_friends)
'''

# Dictionary 
# Dictionary in Python are composed of keys (word) and value (definitions). 
# Dictionaries key must be unique primitive data types (e.g Strings the most common key)
# Dictionaries value can contain any valid python data types 
# Dictionaries are define within curly braces 

'''
mycourses = {'phy101':'Introduction to mechanics', 'csc102':'introduction too computer science', 'matric_no':10000}

mycourses['phy101'] = 'Mechanics'

mycourses['csc203'] = 'Introduction to programming'

mycourses['sta203'] = 'introduction to statistical analysis'

del mycourses['sta203']

print(mycourses)
'''

# Python Operators 
# python supports the following operators 
# * Arithematics * Comparison (relational) * Assignment * Logical * 
# * Bitwise * Membership * Identity 

# Arithematics operators include 
# * Addition * Substraction * Multiplication * Divisionn * Modulus * Exponent (**) * Floor or round off 

# Comparison or relational operators include 
# * Equal (==) * not equal to (!=) * greater than (>) * less than (<) * greater than or equal to (>=)
# * less than or equal to (<=)

# Assignment operators 
# (*) =   (*) +=    (*) -=    (*) /=    (*) %=   (*) **=  (*) //=


# Application 

# A program to calculate the volume of a cylinder 

'''
# import pi from math library 
from math import pi

# Any input from keyboard, input function converts to string 
# So we have to convert it back to a numerical value
# in this case by typecasting it to an integer value 

height = int(input('please enter the height of the cylinder: '))

# same here 
radius = int(input('please enter the radius of the cylinder: '))

# We assign the formular for calculating volume i.e pi * h * r(2) to the variable volume 
volume = pi * height * radius**2

# we print the result of the calculation.
print('The volume of the cube is ', volume)
'''

# A program to store form fill 
# firstname, surname, age, address, state, marital status 

'''

# first step is to create variables to store the input from keyboard 
firstname = input('Enter Firstname: ')
print()
surname = input('Enter Surname: ')
print()
age = int(input('Enter your age: '))
print()
address = input("Enter your home address: ")
print()
state = input('Enter your state: ')
print()
marital_status = input('Enter your marital status: ')
print()

# Save the input data into the dictionary values referencing the variable above 
customer_detail = {'firstname':firstname, 'surname':surname, 'age':age, 'address':address, 'state':state, 'marriage':marital_status}
print(customer_detail['firstname'], customer_detail['surname'])

#increase customers age 
new_age = customer_detail['age']+20
print(new_age)

'''

# Create a data for year starting from 1980 to 2024

'''
years = range(1980, 2024, 2)
year_list = list(years)
print(year_list)
print()

# Creating username using tuple 
username = input('Please enter your username: ')
username = (username, )
print(type(username))
'''

# End of sweet chapter two 