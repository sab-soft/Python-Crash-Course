# Wordking with text file 
# open, read, add and delete an existing text file 

# the open function 
# the open function opens a document and assign it to a file object or handler. 
# the function be in two forms 

# file_name = open('filename.extension')
# file_name = open('filename.extension', 'mode')

# The first form opens in a deffault mode (read)
# the second form opens in a specified mode (recommended)

myfile = open('testfile.txt', 'r')
print(myfile)