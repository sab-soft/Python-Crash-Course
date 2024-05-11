# Slicing is used to access substrings within a string.
# Simply use the square brackets for slicing along with 
# the index or indices to obtain your substring. 

'''
text = 'Python strings are sliceable'

print(text[0])

print(len(text))

l = len(text)
print(text[l-1])
'''

# NOTE: Strings are immutable, and so it is not possible to replace 
# part of a string. However, you can 'update' an existing string by 
# (re) assigning a varriable to another string. The new value can be 
# related to its previous value or to a completely different string altogether 


# Examples 

'''
varr = 'Hello World'

varr = varr[:8] + 'python'

print(varr, ' \a ', '\n', 'Excuse me')
'''

# ESCAPE CHARACTERS: are used to arrange or format our characters in a special way 

# Special String Operators 

# Adding strings: Strings are concatenated using the + sign 
# the modern approach is to use join. join is string method which 
# joins a list of strings(the input) using the object calling the 
# string as the separator 
# join can be used to produce comma separated lists. 

# Adding strings using joins 
'''
a = 'Amakundi'
b = 'samuel'
print(' '.join([a,b]))

# separating list with comma using joins 
statement = ['if', 'I', 'had', 'a', 'chance']
print(','.join(statement))
'''

# Multiplying strings 
# using * 

# formarting Numbers 
# the generic form of a format string is {n:f a swc .p t} or {n:f a swcmt}
# WHERE:
    # n is a number 0, 1, ... indicating which number to take from the format function. 

    # f a are fill and alignment character, typically a 2 character strings. Note: fill 
    # may be any character except }, space is the most common choice. Alignment can <(left)
    # >(right), ^(center), or = (pad to the right of sign). 

    # s indicates whether a sign should be included. where (+ means always include sign), (- included sign if needed)
    # (space indicates to use blank space for positive numbers and - sign for negative sign )
    # this format is useful for producing aligned tables. 

    # m minimum number of size of formated string  

    # c may be or omitted. produces numbers with 1000s separated with a , . in order to use the c it is necessary 
    # to use the (.) before the precision 

    # p is the precision. The interpretation of p depends on t. To use p, it is necessary to include a dot(.) if 
    # if not included it will be interpreted as m.: note precision is not allowed in integer format specifier

    # t is the type. Options include 
        # * exponent notation, e (e+) and E (E+) * 
        # * f, F display number using a fixed number of digits 
        # * g, G General format, which uses f for smaller numbers, and e for larger numbers. G is equivalent to
        # switching between F and E. g is the default format if no presentation format is given. 
        # * n similar to g, except that it uses a locale information. 
        # * % multiplies numbers by 100, and inserts a % sign.

'''
from math import pi

# fill and alignment (f a)
output = '{2:*^50.4f}, {0:*<25}, {1:*>25}'.format(pi, pi+1, 2*pi)

# sign (s)
output1 = '{2: }, {0:+}, {1:-}'.format(pi, pi+1, -2 *pi)

# minimun total size of formated string(m) and separated values with , (c)
# note precision not allowed in interger format specifier 

output2 = '{0:,.30}'.format(100*pi)

value = float(9001)

# complex formating * fill, align to right, use no sign for positive and - or negative 
# minimum of 20 digit, separated by (,), precision of 4 digit figure 
output3 = '{0:*> 20,.4f}'.format(10000 * value)

print(output)
print(output1)
print(output2)
print(output3)
'''


# formating string 
# format output for string formating uses a similar syntax to number formating, although
# some options such as precision, sign, comma, and type are not relevant

'''
name = 12345
print('The formatted string is: {0:*=10}'.format(name))

name = 'Samuel'
print('The formatted string is: {0:*>10}'.format(name))
'''

# Formating multiple objects 
# There are three methods to format multiple objects in the same string output. 
# **** No position arguments, in which case these objects are matched to format string in order. 
# **** Numeric positional argument, in which case the first format object is mapped to '{0:}', 
#      the second to '{1:}', the third to '{2:}' and so on.
# **** Named arguments such as '{firstname:}' and '{surname:}', which match keyword argument inside format. 

'''
firstname = 'Amakundi'
surname = 'Samuel'

# using no position argument
print('My first name is: {:} and my surname is: {:}'.format(firstname, surname))

# using numeric positional argument 
print('My first name is: {0:} and my surname is: {1:}'.format(firstname, surname))

# using numeric positional argument reorder 
print('My surname is: {1:} and my firstname is: {0:}'.format(firstname, surname))

# using named argument 
print('My first name is: {firstname:} and my surname is: {surname:}'.format(firstname=firstname, surname=surname))
'''

# old style format 
# %(map)flm.pt, where 
    # (map) is a mapping string containing a name, for example (firstname)
    # fl is a flag which may be one or more of: 
        # 0 : Zero pad 
        # (blank space)
        # left 
        # + include sign character 

'''
price = 2003.222
volume = 238342

print('The current price is %0.1f with the volume at %d' % (price, volume))

print('The current price is %(price)0.1f with the volume at %(volume)d' % {'price':price, 'volume':volume})

print('The current price is %+0.2f with the volume at %010d' % (price, volume))
'''

# String Methods and Functions
name = 'my name is sabo'
    # capitalize ()     : capitalize first letter of string 
print(name.capitalize())

    # center(width, 'fillchar')   :   Return a space-padded string with the original string centered to a total of width column 
print(name.center(20, '&'))

    # count(word, beg=0, end=len(string))   : count how many times word occurs in a string or in a substring of string if 
    # starting index (beg) and ending index (end) are given. : (sub) is the substring to be searched. (start), (end)
sub = 'me'
print(name.count(sub, 0, len(name)))

    # bytes.decode(encoding="utf-8", errors="strict")   : Decodes the string using the codec registered for encoding. encoding
    # defaults to the default string encoding
fav = 'abumasankari'
utf8_encoded = fav.encode('utf-8')
print(type(utf8_encoded), utf8_encoded)
print()

decoded_fav = utf8_encoded.decode('utf-8')
print(type(decoded_fav), decoded_fav)
print()

    # str.encode(encoding="utf-8", errors="strict")

    # endswith(suffix, beg=0, end=len(string)) : Determines if string or a substring of string endswith with sufffix; 
    # reteurns true if so and false otherwise. 
suffix = ('sabo')
print(name.endswith(suffix, 0, 15))
print()

    # expandtabs[](tabsize=8)     : Expand tabs in string to multiple spaces;
    # defaults to 8 spaces perr tab if tabsize not provided
text = 'This is for \ttab'
print("original text " + text)
print("default tab expanded " + text.expandtabs(16))
print()

    # find(str, beg=0, end=len(string))     : determine iff str occus in string or in a substring of string if starting
    # index beg and ending index end are given returns (index) if found and (-1) otherwise 

mytext = 'do you easy think programming is easy?'
find = 'easy'
print(mytext.find(find))
print()

    # index(str, beg=0, end=len(string))       : same as find(), but raises an exception if str not found. 
print(mytext.index(find))
print()
    # isalnum()     : returns true if string has at least 1 character and all characters are 
    # alphanumeric and false otherwise 

test = 'taughtsolfantationtheor'
print(test.isalnum())
print()

    # isalpha()     : Returns true if string has at least 1 character and all characters are 
    # alphabetic and false otherwise. 
print(test.isalpha())
print()

    # isdigit()     : returns true if strings contains only digit and false otherwise 
dad = '90751877'
print(dad.isdigit())
print()

    # islower()     : returns true if string has atleast 1 cased character and all cased characters are in 
    # lowercase and false otherwise 

toast = 'excellent'
print(toast.islower())
print()

    # isnumeric()   : returns true if a unicode string contains only numeric characters and false otherwise 

unicode = u'070338890'
print(unicode.isnumeric())
print()

    # isspace()     : returns true if a string contains only white space and false otherwise 
spacial = '  4  '
print(spacial.isspace())
print()

    # istitle()     : returns if string is properly 'titlecased' and false otherwise.
topic ='Corporal Punishment And Disciple'
print(topic.istitle())
print()

    # isupper()     :   returns true if string is properly 'titlecased' and false otherwise. Returns true if string 
    # has at least one cased character and all cased characters are in uppercase and false otherwise. 
gist = 'CORPORAL PUNISHMENT'
print(gist.isupper())
print()

    # join()    :   Merges(concatenates) the string representations of elements in sequence seq into a string, 
    # with separator string 
s = '-'

sequ = ('ama', 'kun', 'di')

print(s.join(sequ))
print()

    # len(string)   : returns the length of the string
lenggth = 'Amak knows nno bound'
print(len(lenggth))
print()

    # ljust(width[.fillchar])   :   returns a space-padded string with the original sting left-justified to a total of width columns
name = 'DEBORAH'
print(name.ljust(50, '*'))
print()

    # lower()   :   converts all uppercase letters in string to lowercase 
print(name.lower())

    # lstrip()  : removes all leading whitespace in string or returns a copy of the string in which all chars have been 
    # stripped from the beginning of the string 
'''
str = '        this is a sample!    *'
print(str.lstrip())
print()

str2 = '******* this is also a sample *****'
print(str2.lstrip('*'))
print()

    # maketrans()   :   returns a translation table to be used in translate function
intab = 'aeiou'
outtab = '12345'

trantab = str.maketrans(intab, outtab)

string = 'this is strring example!!! amak aaaaaaaaa undi'
print(string.translate(trantab))
print()
'''

    # max(str)  : returns the max (in alphabetical order) alphabetical character from the string str
'''
maximum = 'amakundibakoyhhhh*'
print(max(maximum))
print()

    # min(str)  :   returns the min  alphabetical (least) character from the string str
print(min(maximum))
print()

    # replace(old, new[,max])   :   replaces all occurrences of old in string with new or at 
    # most max occurrences if max given 

print(maximum.replace('a', 'i'))
print(maximum.replace('h', 'u', 2))
print()
'''

    # rfind(str, beg=0, end=len(string))    :   same as find(), but search backwards in string 

    # rindex(str, beg=0, end=len(string))   :   same as index(), but search backwards in string 

    # rjust(width, [, fillchar])    :   returns the string right jusified in a string of length width. 

    # rstrip()  : returns a copy of the string in which all chars have been stripped from the end of the string.
    # default whitespace characters

    # split(str='', num=string.count(str))  : splits string according to delimiter str (space if not provided) and 
    # returns list of substrings; split into at most num substing if given 
'''
splitti = 'line1 line2 and line3'
print(splitti.split())
print(splitti.split(' ', splitti.count(splitti)))
print()


    # splitlines(num=string.count('\n'))    : splits string at all (or num) newlines and returns a list of 
    # each line with newlines removed 
var = 'line 1 2 f\n3 4 lin\n\nne'
print(var.splitlines())
print(var.splitlines(0))
print(var.splitlines(3))
print()
'''

    # startswith(str, beg=0, end=len(string))   : determines if string or a substring of string starts wiith 
    # substring str; returns true if so and false otherwise 

    # strip([chars]) :   performs both lstrip() and rstrip() on string 
'''
name = ' #   amastone *****'
print(name.strip(' *#'))
print()

    # swapcase()    : inverts case for all letters in string 
swap = 'AmaKundi'
print(swap.swapcase())
print()
'''

    # title()   : returns 'titlecased' version of string, that is, all words 
    # begsins with uppercase and the rest are lowercase 

    # translate(table, deletechars = '')    : translates string according to translation table str(256 chars), 
    # removing those in the del string 
'''
intab = 'aeiou'
outtab = '12345'

trantab = str.maketrans(intab, outtab)

str = 'this is string example ...!'

print(str.translate(trantab))
print()

# to delete a string from the string
str = 'this is string example ...!'
print(str.translate(trantab, 'ex'))
print()
'''
    # upper()   : converts lowercase letters in string to uppercase 

    # zfill(width)  : returns original string leftpadded with zeros to a total of width characters; intended for 
    # numbers, zfill() retains any given given (less one zero) 

    # isdecimal()   : returns true if a unicode string contains only decimal characters and false otherwise 

# APPLICATION 

# Example 1: Creating an editor 
'''
print("**************** MENU ******************")
print("    (1) Upper Case                      ")
print("    (2) Lower Case                      ")
print("    (3) Titlecased                      ")
print("    (4) Swap case                       ")
print("    (5) Exit\n                          ")
print("**************** MENU ******************")

# Variable to store menu option inputed 
menu = int(input("Enterr the option from the MENU: "))

# while loop to check number inputed 
while (menu != 5):

    # block to verify number inputed 
    if (menu in range(1, 6)): 
        text = input("Enter your sentence:\n ")
        
        # Change sentence to upper case 
        if (menu == 1):
            print(text.upper())

        # Change sentence to lower case 
        elif (menu == 2):
                print(text.lower())
        
        # change sentence to title case 
        elif (menu == 3):
                print(text.title())
        
        #Change sentence to swap case 
        elif (menu == 4):
            print(text.swapcase())
        
        # option to continue editor or exit 
        menu = int(input('Enter another option to continue: '))

    else:
        menu = int(input('Your input is out of range, enter option 1 -5 '))
    
print("Goodbye!")
'''

# Example 2 : print a table 
# create a list of the table 
'''
record = [['amakundi', 253], ['samuel', 532], ['bako', 323], ['caleb', 164]]

# Print header 
nam = len('names')
print("names", "*"*(22-nam), "Total score")
print()

# print the rows and columns 
# iterate through the number of item in record 
for item in record: 
     
     # print item at [0] and item at [1] for spacing give a total of 
     # 14 spaces minus the length of the string (item) at index [0]
     print(item[0], '*'*(22-len(item[0])), item[1])
     print()
'''

# A program to guess a random number and ring a bell if the guess is wrong

# special library to generate random numbers 
from random import *

# system to generate a random number between 1 and 10 
getrand = randint(1, 10)

print(getrand)

num = int(input("Enter a random number between 1 and 10: "))

if (num == getrand):
    print("Well done! Your guess is correct")
else: 
    print("\a")
    print("incorrect")
    print("The correct number is {:}, Please try again!!".format(getrand))