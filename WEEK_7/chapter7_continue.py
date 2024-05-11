# working and visualizing excel file and data 

# example of python module for working with excel files 
# openpyxl, pandas, xlwt and xlrd 

# NOTE: make sure the excel file you are working with is not opened on your computer 
# 
import openpyxl

object = openpyxl.load_workbook('my_data.xlsx') 

# get workbook active sheet object from the active attribute 
active_object = object.active

# NOTE: the first row or column integer is 1, not 0. 
# cell object is created by using sheet object's cell() method 

cell_object = active_object.cell(row=1, column=1)
print(cell_object)

import pandas 