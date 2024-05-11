# Exercise one: Calculate the volume of a cuboid 
# Given that volume of cuboid is v = lwh 

# Get data input from keyboard 
'''
length = int(input('Please enter length: '))
print()
weight = int(input('Please enter weight: '))
print()
height = int(input('Please enter height: '))

# formula for calculating volume of cuboid 
volume = length * weight * height

print(volume)
'''

# user registration form 
# username, password, firstname, surname, age, address, state, marital_status 
# note: username and password should be tuple since they are rarely changed
username = input('Please enter your username: ')
username = (username,)
print()
password = input('please enter your password: ')
password = (password,)
print()
firstname = input('Enter your firstname: ')
print()
surname = input('Enter your surname: ')
print()
age = int(input('Enter your age: '))
print()
address = input('Enter your home address: ')
print()
state = input('Enter your state:')
print()
marital_status = input('Enter your marital status')
print()

# Assign user data to a dictionary 
user_record = {'username': username, 'password': password, 'firstname':firstname, 'surname':surname, 'age':age, 'address':address, 'state':state, 'marriage':marital_status}

print(user_record)

# End of chapter two exercises