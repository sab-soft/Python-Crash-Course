# function format 
# def functionname ( paramaters ):
#   "function docstring"
#   function suite
#   return [expression]

# function with argument 
# 

# function with return 
# code after the return statement will not be executed 

# function as object 


# module 


# APPLICATON

# Program go calculate electricity tariff
'''
def cal_tariff(amount):
    bill = kwh * tariff
    
    return bill

tariff = 200

kwh = int(input("Please enter your elec. cons. in kwh: "))

cost = cal_tariff(kwh) 

if cost <= 2000:
    print("Your bill is free")
else:
    print("Your bill is: ", cost)
'''

# A program to display menu, add, multiply and subtract 

# simple calculator function to add and multiply two numbers 
# option is parameter for menu selection
# first_number is parameter for first number
# second_number is parameter for second number 

def calculator(option, first_number, second_number):
        
            if option == 1:
                add = first_number + second_number
                return add
            
            else:
                multiply = first_number * second_number
                return multiply

# Function to display menu option                     
def display_menu():     
    print("************* Menu **********************")
    print("********(1)   Add ***********************")
    print("********(2)   Multiply ******************")
    print("********(3)   Exit **********************")
    print()
    print("Please enter an option to continue ")

# Call the function display_menu 
display_menu()

# Accept option menu from the user 
option_selected = int(input("Select option: "))

# first loop (while) checks if selection is to proceed or exit application
while option_selected != 3:

    # this condition check to make sure selection is either one or two 
    if option_selected in range(1, 3):
        
        # Accept the two operand from the user 
        operand_one = int(input("Enter your first operand: "))
        operand_two = int(input("Enter your second operand: "))

        # If selection is one then perform addition 
        if (option_selected == 1):
            # Call the calculator function to perform addition 
            # supplying the three parameter option, first_number
            # and second number
            result = calculator(option_selected, operand_one, operand_two)
            print("Addition of {} and {} is: {}".format(operand_one, operand_two, result))
                
        # if selection is two then perform multiplication 
        if(option_selected == 2):
            # call the function calculator supplying the three parameters 
            # with the arguments 
            result = calculator(option_selected, operand_one, operand_two)
            print("Multiplication of {} and {} is: {}".format(operand_one, operand_two, result))

        # Ask if user wants to continue calculation
        option_selected = int(input("Select an option to continue: "))
    
    # Ask user to re-enter selection if selection is not a valid option 
    else:
         option_selected = int(input("Please select valid option: "))

print()
# Exit application if option selected is three 
print("Good bye from calculator")