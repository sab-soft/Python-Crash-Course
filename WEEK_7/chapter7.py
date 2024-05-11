# Wordking with text file 
# open, read, add and delete an existing text file 

# the open function 
# the open function opens a document and assign it to a file object or handler. 
# the function be in two forms 

# file_name = open('filename.extension')
# file_name = open('filename.extension', 'mode')

# The first form opens in a deffault mode (read)
# the second form opens in a specified mode (recommended)

'''
myfile = open('testfile.txt', 'r')
print(myfile)
myfile.close()
'''

# Modes 
# r     : opens a file for reading only. The file pointer is placed at the beginning of the 
#       file. This is the default mode. 

# rb    : Opens a file or reading only in binary format. The ffile pointer is placed at the
#       beginning of the file. This is the default mode. 

# r+    : Opens a file for both reading and writing. The file pointer placed at the beginning 
#       of the ffile. 

# rb+   : Opens a file for both reading and writing in binary format. The file poinnter placed
#       at the beginning of the file. 

# w    : Opens a file for writing only. Overwrites teh file if the ffile exists. If the file 
#       does not exist, creates a new file for writing. 

# wb    : Opens a file for writing only in binary format. Overwrites the file if the file exists. 
#       If the file does not exist, creates a new file for writing. 

# w+    : Opens a file or both writing and reading. Overwrites the existing file if the file exists. 
#       If the ffile does not exist, creates a new file for reading and writing. 

# wb+   : Opens a file for both writing and reading in binary format. Overwrites the existing file 
#       if the file exists. If the file does not exist, creates a new file for reading and writing. 

# a     : Opens a file for appending. The file pointer is at the end of the file if the file exists. 
#       That is, the file is the append mode. If the file does not exist, it creates a new file for writing. 

# ab    : Opens a file for appending in binary format. The file pointer is at the end of the file if the 
#       file exists. That is, the ffile is in the append mode. If the file does not exists, it creates 
#       a new file for writing. 

# a+    Opens a file for both appending and reading. The file pointer is at the end of the file if the 
#       file exists. The file opens in the append mode. If the file does not exist, it creates a new file 
#       for reading and writing.

# ab+   : Opens a file for both appending and reading in binary format. The file pointer is at the end of 
#       the file if the file exists. The file opens in the append mode. If the file does not exist, it 
#       creats a new file for reading and writing. 

# NOTE: all modes are in small case letters 
# NOTE: you have to explicitly close the handler

# open file using a context manager
# NOTE: this is best practices 

'''
with open('testfile.txt', 'r') as myfile:
    pass
print(myfile.closed)
'''

# Reading the content of file 
# load all content of file to memory at once

'''
with open('testfile.txt','r') as myfile:
    content = myfile.read()
    print(content)
    print()
'''

# read content with readline 
# This reads only one line at a time. the next line 
# is printed by reading the content (file) again.

'''
with open('testfile.txt','r') as myfile:
    content = myfile.readline()
    print(content, end='')
    content = myfile.readline()
    print(content, end='')
    print()
'''
     
# read content with readlines
# reads all lines with the \n character to inform you of a new line. 
# NOTE: reading by readline is time consuming whereas reading by readlines consumes memory 

'''
with open('testfile.txt','r') as myfile:
    content = myfile.readlines()
    print(content)
    print()
'''

# using for loop to print line by line 
# read one line each time to memory 

'''
with open('testfile.txt','r') as myfile:
    for line in myfile:
        print(content, end='')
        print()
'''

# reading file using read + an argument to read a chunk at a time 
# reads the irst 100 character in myfile 

'''
with open('testfile.txt','r') as myfile:
    content = myfile.read(100)
    print(content, end='')
    print()
'''

# read a chunk of file 
# prints return an empty string if the end of the file read 
# to avoid that; we loop and set a condition to check for the empty string

'''
with open('testfile.txt','r') as myfile:
    chunk_to_read = 100
    content = myfile.read(chunk_to_read)

    while len(content) > 0:
        print(content, end='') # end='*' appears after every 100 character
        content = myfile.read(chunk_to_read)
'''


# Tell command 
# handler.tell()
# use this command to check the current positions of the counter/pointer in the file  

'''
with open('testfile.txt','r') as myfile:
    chunk_to_read = 100
    content = myfile.read(chunk_to_read)
    print(myfile.tell())
    print()
'''
    
# seek command 
# the seek command can take the pointer to a new position other than advancing the pointer.
# handler.seek()

'''
with open('testfile.txt','r') as myfile:
    chunk_to_read = 100
    content = myfile.read(chunk_to_read)
    print(myfile.tell())
    
    content = myfile.read(chunk_to_read)
    print(myfile.tell())
    
    myfile.seek(2)
    content = myfile.read(chunk_to_read)
    print(myfile.tell())
    print()
'''
    
# Writing to file 
# handler.write() command to write to a file
# NOTE: if the ile does not exist the write mode will create the file.
# NOTE: If it does exist, the ffile will be replaced. 
# NOTE: change the mode to lower case 'a' to append rather than replacing file content 

# creating a new file with a title 

'''
with open("newfile.txt", "w") as myfile2:
    myfile2.write('Welcome back to the section of working with filese \
        in this course. We hope it has been interested all the way.')
    
    myfile2.write('By December, I should be able to code in python \
        at least as an intermediate.')
    
    myfile2.write('consistency breed perfection')
    
    myfile2.seek(0)
    myfile2.write("WELCOME BACK BUMA ")
    
with open("newfile.txt", "r") as readnewfile:
    cont = readnewfile.readlines()
    print(cont)
'''

with open('welcome.txt', 'w') as firstfile:
    show = firstfile.write("Welcome to python programming")
    print(show)
    
with open('welcome.txt', 'r') as secondfile:
    with open('welcome2.txt', 'w') as thirdfile:
        for line in secondfile: 
            show1 = thirdfile.write(line)
            print(show1)
            print()
            
with open('success.jpg', 'rb') as myownfile: 
    with open('pexcopy.jpeg','wb') as thefile: 
        for line in myownfile:
            thefile.write(line)
            
            
with open('success.jpg', 'rb') as myownfile: 
    with open('pexcopy2.jpeg','wb') as thefile: 
        chunk_size = 4096 #4bytes (1byte = 1024bits)
        the_chunk = myownfile.read(chunk_size)
        while len(the_chunk) > 0:
            thefile.write(the_chunk)
            the_chunk = myownfile.read(chunk_size)
            
# Adding to an existing file 
# the + sign in a+ indicates that the file should be created if it does not exist however,
# in our case it exist already so you should see this ....
with open('testfile.txt', 'a+') as mynewfile:
    varnew = mynewfile.write('\n. This is the new line rom chapter 6')
    print(varnew)
    
# Deleting lines ffrom an existing file 
# the remove function can also be used to remove a file from your systems. 
# however, you need to write out the path to the file except if the file is in 
# your current working directory. To simply remove a file from the current directory you need 
# to import os then remove the file by os.remove

with open ('testfile.txt', 'r') as mynewffile:
    lines = mynewffile.readlines()
    lines.remove('. This is the new line rom chapter 6')
    with open('testcopy.txt', 'w') as mywritefile:
        for line in lines: 
            mywritefile.write(line)
    
# removing a file 
import os 
os.remove('pexcopy2.jpeg')

# renaming file 
import os 
os.rename('currentname.extension', 'newname.extention')
