# enter departure and arrival cities, and select tavel dates 
# Browse  flight options and select your ideal flight 
# insert correct passenger details (as per ID)
# select any additional add-ons like insurrace or exta baggage 
# confirm your prefferred payment method 
# Receive your e-ticket straight to your inbox. Off you go! 

# declaring variables 

# Name of airport 
airline = 'BumaAirlines'

# names of departure and arrival cities 
depart_arrival_city = [['Wukari', 'Jalingo', 'Abuja', 'Adamawa', 'Lagos'], ['Jalingo', 'Abuja', 'Lagos', 'Abuja', 'Jalingo']]

# payment methods 
payment = ['Card', 'USSD', 'Electronic Transfer', 'Internet Banking']

# names of people in flight 
flight_list = {}

# Seat capacity of plane 
seat_capacity = 21

# Seat already booked
booked_seat = []

# List of books available for reading 
list_of_reading_list = [['News: ', 
                        'Sport: ',
                        'Science: ',
                        'Technology: '], 
                        ['How to succeed as entreprenure in Nigeria', 
                         ' How nto become skilled liked Ronaldo',
                         'My experience of travelling to the mooon',
                         'Have you considered learning python programming language']]

# Title of the user 
title = ['Mr', 'Mrs', 'Ms', 'Miss', 'Dr']

# Ask user to enter his name 
firstname = input('Dear User, Please enter your firstname: ')
surname = input('Dear user, please enter your surname: ')

# Ask for the user's title 
print('Please enter select your title from the option below')
print('*************(1) ', title[0])
print('*************(2) ', title[1])
print('*************(3) ', title[2])
print('*************(4) ', title[3])
print('*************(5) ', title[4])
print()

user_title = int(input('Select: '))

while (user_title == user_title):

    if (user_title in range(1, 6)):
    
        initial = surname + ', ' + firstname[0]
        initial = initial.strip('')

        print('Hello! Dear   {0:} {1:}'.format(title[user_title-1], initial.upper()))
        print('Welcome to    {0:}'.format(airline))
        print()

        break
    else:
        user_title = int(input('Please select one of the option above: '))

# Selecting departure and arrival cities 
departure = depart_arrival_city[0][:]
arrival = depart_arrival_city[1][:]

print('Please select your Departure and Arrival city from the menu below') 

print('*************(1)  From', departure[0], '\tto',  arrival[0])
print('*************(2)  From', departure[1], '\tto',  arrival[1])
print('*************(3)  From', departure[2], '\tto',  arrival[2])
print('*************(4)  From', departure[3], '\tto',  arrival[3])
print('*************(5)  From', departure[4], '\tto',  arrival[4])
print()

#amount = {'WJ':3000, 'JA':5000, 'AL':2300, 'AA':3032, 'LJ':3000}
fc2c = ['WJ', 'JA', 'AL', 'AA', 'LJ']
amount = [3000, 5000, 2300, 3032, 3000]

destination = int(input('Please enter your destination: '))

while (destination == destination):

    if (destination in range(1, 6)):
        
        destination = destination - 1
        print('You selected the following destination: From', departure[destination], 'to', arrival[destination])
        print('Amount is: ', amount[destination])
        print()

        break
    else:
        destination = int(input('Please select one of the option above: '))

print('Please how would you like to pay')
print('Please select your payment method from the option below')
print('*************(1) ', payment[0])
print('*************(2) ', payment[1])
print('*************(3) ', payment[2])
print('*************(4) ', payment[3])
print()

pay_method = int(input('Please select an option above: '))
while (pay_method == pay_method):

    if (pay_method in range(1, 5)):

        pay_method = pay_method -1 
        print("Redirecting you to the payment gateway: ")
        print("Payment successful")
        print("Your", payment[pay_method], 'payment was successful')
        print('')
        break
    else: 
        pay_method = int(input('Please select an option above: '))