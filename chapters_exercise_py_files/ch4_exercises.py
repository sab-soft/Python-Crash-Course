# Write a program to request first name and last name from a user. 
# Create an initial using the first and last name. 

# create two variable for first name and second name 
'''
firstname = input("Enter your first name:\n")
lastname = input("Enter your last name:\n")

initials = firstname[0] +'.' + lastname[0]
print("Your initials are: ", initials.strip(' ').upper() )
'''

# A program that returns the length of sentences and prints the longest one 
'''
fsentence = 'i am learning python programming'
ssentence = 'python progrram is simple and easy'

fsen_len = len(fsentence)
ssen_len = len(ssentence)

if (fsen_len > ssen_len):
    print('first sentence has {:} length and second sentence has {:} length.'.format(fsen_len, ssen_len))
    print('The longest sentence reads: ', fsentence)
else:
    print('first sentence has {:} length and second sentence has {:} length.'.format(fsen_len, ssen_len))
    print('The longest stenence reads: ', ssentence)
'''

# Write a python program to get the last part of this string 
# "https://www.tutorialspoint.com/python/python_strings.htm"
'''
var = "https://www.tutorialspoint.com/python/python_strings.htm"
list_var = var.split('/')
print(list_var)
count = len(list_var)
print("The last part of the String {:} is: ".format(var), list_var[-1], '\nWhich is splitted into {:}.'.format(count))
'''

# Program to print integers with zeros on the left of specified width of 6 
'''
intnumbers = [1, 23, 450, 2456]

for num in intnumbers: 
    print('{0:0>6}'.format(num))
'''

# program to display the number 05 in left, right and center aligned of width 10 
'''
var = '*5'
print('{0:0<10}, \n {0:0>10}, \n {0:0^10}'.format(var))
'''

# program to display formated text (width=20)
'''
string = 'Our greatest weakness lies in giving up. The most certain way to succeed is always\
    to try just one more time'
print('{0:.20}'.format(string))
'''
# a program to swap comma and dot in a string
'''
intab = ',.'
outtab = '.,'

trantab = str.maketrans(intab, outtab)

string = '$456.045,00 #456,045.00'

print(string, 'swap to', string.translate(trantab))
'''

# swaping 
alpha = '0a/0b/0c/0d/0e/0f/0g/0h/0i/0j/0k/0l/0m/0n/0o/0p/0q/0r/0s/0t/0u/0v/0w/0x/0y/0z'
num = '01/02/03/04/05/06/07/08/09/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26'

a = alpha.split('/')
n = num.split('/')

intab = str(a)
outtab = str(n)

s = '**'

trantab = str.maketrans(intab, outtab)

string = 'amakundi'

print(s.join(string.translate(trantab)))