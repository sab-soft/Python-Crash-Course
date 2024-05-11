# Flow control in Python comes in two form 
# Decision Making and Loop 
# Decision makeing include if statements, if else, elif statements, and nested if statements
# Loop inlude while loop, for loop and nested loop 

# Bitwise operator: Perform bit by bit operation 

# LOGICS : OR(|), AND(&), XOR(^), NOR(~), Binary left shift (<<), Binary right shift 

# Membership operator: There are two membership operators * in * not in 
# Membership evaluates to true or false when assigned to a variable respectively 

# Identity operator: This operator compare the memory location of two objects. 
# They include: is, is not 
# Evaluates to true if the variables at either side of the operator point to the same 
# object and false otherwise. 

# Decision Making 

# If Statement : An if statement consists of a boolean expression followed by 
# one or more statements 

# If else statement : An if statement followed by an else statement, 
# An else statement is the block of code that executes if the conditional expression 
# in the if statement results to false (0). The else statement is an optional stament and 
# there could be at most only one else statement following if. 

# elif statement: The elif statments allows you check multiple expressions for TRUE and 
# execute a block of code as soon as one of the conditions results to TRUE. There can be 
# an arbitrary number of elif statements following an if. 

# Loops  : A loop statements allows us to execute a statement or group of statements multiple times.
# Types of Loops 
# For loops: Executes a sequence of statements multiple times and abbreviate the code that manages the loop variables.
# While loops: Repeat a statement or group of statements while a given condition remain TRUE. It tests the condition
# before executing the loop body. 
# Nested loops: Loops inside loop ...

'''
liste = [1, 2, 3, 4]

for n in liste:
    print('I love coding', n)

for letter in 'Amakundi':
    print('The letter in the word Amakundi is: ', letter)
'''

'''
count = 0

while (count <5):
    print('welcome 00', count)
    count += 1
print('Goodbye')
'''

'''
var = 0 

while (var == 0):
    number = int(input('Enter a number: '))
    print('You entered the number ', number)

print('Goodbye')
'''

'''
count = 0

while (count < 5):
    print('You entered the number: ', count)
    count += 1
else:
    print('Goodbye')
'''

# Break Statement 
# Terminates the loop statements and transfers execution to the statement 
# immediately following the loop 
# Break can be used in both while and for loops 
# If you are using nested loop, the break statement stops the execution of 
# the innermost loop and start executing the next line of code after the block.

# Continue Statement 
# Causes the loop to skip the remainder of it's body and retest its condition 
# prior to reiterating 

# Pass Statement 
# The pass statement in python is used when a statement is required syntactically 
# but you do not want any code or command or statement to execute 
# it is a null operation; nothing happens when it executes. 
# Useful, where your code will go but has not been written yet. 



'''
for letters in 'python': 
    if (letters == 'h'):
        print('I have found the letter', letters)
        continue
    else:
        print('I haven\'t found the letter yet. ')
'''

'''
var = 10

while (var > 0):
    print('current variable value', var)

    var -= 1

    if var ==5:
        break
print('Goodbye')
'''

'''
for letters in 'python':
    if letters == 'h':
        continue
    print('current letter', letters)

var = 10 

while (var > 0):

    var -= 1

    if var == 5: 
        continue

    print('The current variable value is ', var)

print('Goodbye! ')
'''

'''
for letters in 'python': 

    if letters == 'h':

        pass 
        
        print('This is a pass block')
        continue
    
    print('current letter is ', letters)

print('Goodbye')
'''

# try ... except 
# These blocks are useful for running code which may fail or reasons 
# outside of the programmes control


text = ('a', '4', '4.a', '4.5')

for t in text:

    try:
        temp = float(t)
        print(temp)

    except ValueError:
        print('Cannot convert to a float')


# Apllication 

# Program to assign grade to a score 

'''
# Receive input from the user 
score = int(input('Please enter your score: '))

A = list(range(75, 101))
AB = list(range(70, 75))
B = list(range(65, 70))
BC = list(range(60, 65))
C = list(range(55, 60))
CD = list(range(50, 55))
D = list(range(45, 50))
E = list(range(40, 45))
F = list(range(0, 40))

if (score in A):
    print('Your score is: ', score, 'Your grade is: ', 'A')

if (score in AB):
    print('Your score is: ', score, 'Your grade is: ', 'AB')

if (score in B):
    print('Your score is: ', score, 'Your grade is: ', 'B')

if (score in BC):
    print('Your score is: ', score, 'Your grade is: ', 'BC')

if (score in C):
    print('Your score is: ', score, 'Your grade is: ', 'C')

if (score in CD):
    print('Your score is: ', score, 'Your grade is: ', 'CD')

if (score in D):
    print('Your score is: ', score, 'Your grade is: ', 'D')

if (score in E):
    print('Your score is: ', score, 'Your grade is: ', 'E')

if (score in F):
    print('Your score is: ', score, 'Your grade is: ', 'F')
'''

# Simple addition and multiplication calculator 


print('************************* MENU *************************')
print(' (1)   Addition                  ')
print(' (2)   Multiplication            ')
print(' (3)   Exit Application')

# take input from user 
menu = int(input('Enter the menu options to proceed: '))

# main loop 
while (menu != 3):

    # Check if the number inputed is in the range of menu options
    if (menu in range(1, 3)):
        
        # Take first and Second number 
        firstnumber = int(input('Enter the first number: '))
        secondnumber = int(input('Enter the second number: '))

        # verify option selected and carryout operation
        if (menu == 1):
            total = firstnumber + secondnumber
            print('Addition of: ', firstnumber, '+', secondnumber, '=', total)
        
        # verify option selected and carryout operation
        if (menu == 2): 
            total = firstnumber * secondnumber
            print('Multiplication of: ', firstnumber, '*', secondnumber, '=', total)

        menu = int(input('Enter the menu options to continue: '))

    # if number inputed is not in range of menu option
    else:
        menu = int(input('Enter the menu option to continue'))

print('Thank you and goodbye')


# program to calculate electricity bill 

'''
tariff = 200 

consump_kwh = int(input('Enter your electricity consumption rate in kWh: '))

bill = consump_kwh * tariff

print('Your bill total bill is: #', bill )

if (bill<=2000):
    print('your bill is FREE!')
'''