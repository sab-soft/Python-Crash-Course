# This is my first comment in FPC 

'''
This is my first comment in FPC 
I hope to be a professional python programmer by December, 2024. 
I will work hard and smart to complete the course. 
'''

# Working with variables 
"""
Variables names can take many forms. They can contain numbers, letters (both lower and uppercase) and underscore (_)
"""

"""
# Assigning values to variables or initializing variables 
name = "Amakundi"
age = 25 
weight = 60.5
print(name, age, weight)

# Assigning multiple variables 
name, age, weight = "Amakundi", 25, 60.5 
print(name, age, weight)

# Taking input from the keyboard and assigning to a variable 
name = input("Please enter your name ")
print(name)

# Taking input for name and age 
name = input("Please enter your name ")
age = input("Please enter your age ")

print("Your name is ", name, "your age is ", age)
"""

# Exploring data types in python 
# numeric, boolean, set, dictionary, sequence 
# numeric data types include integers, float and complex numbers 

"""
age = 25 
print(type(age))

weight = 60.22
print(type(weight))

name = "Samuel Amakundi Bako" 
print(type(name))

list = [1, 2, 3, 4, 5]
print(type(list))

tuple = (1, 2, 3, 5)
print(type(tuple))

complex = 10J
print(type(complex))
"""

"""
# Boolen data represent true or false 
x, y = True, False 
print(x)
print(y)
print(type(x))
"""

# Sequence data types 
# Strings, List and Tuples 

"""
name = "Amakundi" 
surname = 'Samuel' 
print(name, surname)

list = [23, 24, 30, 'amakundi', 'samuel', 22.2, 1.0]
print(list[2])

list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
print(list)
print(list[0][3], list[1][3])
"""

# 2D list/array
"""
students_score = [['james', 'john', 'amakundi'], [20, 30, 40]]
name = students_score[0][1]
score = students_score[1][1]
print("Your records are as follows", 'name = ', name, 'score = ', score)
"""

# Concatenating a list 
"""
list_one = ["Amakundi", "Samuel", "Bako"]
list_two = ["love", "coding", "in"]
concatenated = list_one + list_two 
print(concatenated)
"""

# Repetition of list 
"""
list_one = ['list', 'variable', 'data']
repeat = 5 * list_one
print(repeat)
"""

# Checking an item in a list using keyword 'in'
"""
list = [1, 2, 'samuel', 'coding', 50, 55]
print('samuel' in list)
print('bako' in list)
print(50 in list)

slice1 = list[:]
slice2 = list[1]
slice3 = list[0:]
slice4 = list[:len(list)]
slice5 = list[0:4]
slice6 = list[0:len(list):2]

print('First slice ', slice1)
print("second slice ", slice2)
print("third slice", slice3)
print(slice4, slice5, slice6)

slice7 = list[-4]
print("this slice ", slice7)
"""

# List Functions 
# append, pop, remove, del slice, extend, count, len

'''
family = ['samuel', 'jemimah', 'larai', 'tubasen', 'fosen', 'amakundi']
new_family = family.append('miracle')
print(family)
print('There are ', len(family), 'people in your family')

new_family_members = family.extend(['miracle', 'ndeyima'])
print(sorted(set(family)))

new_family = family.pop(3)
print(new_family)
print(family.count('miracle'))

del family[4:-1]
print(family)
'''

"""
# Application of work learnt 
# Program to record the names and scores of students in class 

students_name = ['Amakundi', 'Samuel', 'Bako', 'Amaaku', 'Felix', 'Uhwe']
students_score = [30, 50, 60, 70, 80, 10]
"""

"""
print('Table')
print("     " 'Name' "     " 'Score')
print("     ", students_name[0], "\t", students_score[0] )
print("     ", students_name[1], "\t", students_score[1] )
print("     ", students_name[2], "\t", students_score[2] )
print("     ", students_name[3], "\t", students_score[3] )
print("     ", students_name[4], "\t", students_score[4] )
print("     ", students_name[5], "\t", students_score[5] )
"""
# Append new names and scores to the existing lists 
"""
students_name.append("Victoria")
students_score.append(80)

print(students_name, students_score)
"""

# Extend the list by 4 additional names and scores 

'''
students_name.extend(['faith', 'john', 'victor', 'festus'])
students_score.extend([50, 40, 80, 90])

print(students_name, students_score)
print(len(students_name))
print(len(students_score))

# First five names and scores of students 
first_five_names = students_name[:5]
first_five_scores = students_score[:5]
print(first_five_names)
print(first_five_scores)

del students_name[-3:]
del students_score[-3:]
print(students_name)
print(students_score)

# Concatenate the two list 
students_data = [[students_name], [students_score]]
print(students_data)

# End of chapter one
'''