# A program to display menu, add, multiply, subtract, divide and exit 

# simple calculator function to add and multiply two numbers 
# option is parameter for menu selection
# first_number is parameter for first number
# second_number is parameter for second number 

'''
def calculator(option, first_number=0, second_number=0, third_number=0):
        
            if option == 1:
                add = first_number + second_number + third_number
                return "{0:*^+20,.5f}".format(add)

            elif option == 2:
                multiply = first_number * second_number * third_number
                return "{0:*^+20,.5f}".format(multiply)

            elif option == 3:
                 subtract = first_number - second_number - third_number
                 return "{0:*^+20,.5f}".format(subtract)

            else:
                divide = first_number / second_number / third_number
                return "{0:*^+20,.5f}".format(divide)

# Function to display menu option                     
def display_menu():     
    print("************* Menu **********************")
    print("********(1)   Add ***********************")
    print("********(2)   Multiply ******************")
    print("********(3)   Subtract ******************")
    print("********(4)   divide ********************")
    print("********(5)   Exit **********************")
    print()
    print("Please enter an option to continue ")

# Call the function display_menu 
display_menu()

# Accept option menu from the user 
option_selected = int(input("Select option: "))

# first loop (while) checks if selection is to proceed or exit application
while option_selected != 5:

    # this condition check to make sure selection is either one or two 
    if option_selected in range(1, 5):
        
        # Accept the two operand from the user 
        print("Please enter two or three integers to perform calculation: ")
        print("Enter 00 to submit numbers")

        operand_one = int(input("Enter your first operand: "))
        operand_two = int(input("Enter your second operand: "))
        operand_three = int(input("Enter your third operand: "))

                             
        # If selection is one then perform addition 
        if (option_selected == 1):
            # Call the calculator function to perform addition 
            # supplying the three parameter option, first_number
            # and second number
            result = calculator(option_selected, operand_one, operand_two, operand_three)
            print("Addition of {} {} and {} is: {}".format(operand_one, operand_two, operand_three, result))
                    
        # if selection is two then perform multiplication 
        if(option_selected == 2):
            # call the function calculator supplying the three parameters 
            # with the arguments 
            result = calculator(option_selected, operand_one, operand_two, operand_three)
            print("Multiplication of {} {} and {} is: {}".format(operand_one, operand_two, operand_three, result))

        if (option_selected == 3):
            # Call the calculator function to perform subtraction 
            # supplying the three parameter option, first_number
            # and second number
            result = calculator(option_selected, operand_one, operand_two, operand_three)
            print("Subtraction of {} {} and {} is: {}".format(operand_one, operand_two, operand_three, result))

        if (option_selected == 4):
            # Call the calculator function to perform division 
            # supplying the three parameter option, first_number
            # and second number
            result = calculator(option_selected, operand_one, operand_two, operand_three)
            print("Division of {} {} and {} is: {}".format(operand_one, operand_two, operand_three, result))

        # Ask if user wants to continue calculation
        option_selected = int(input("Select an option to continue: "))
    
    # Ask user to re-enter selection if selection is not a valid option 
    else:
         option_selected = int(input("Please select valid option: "))

print()
# Exit application if option selected is three 
print("Good bye from calculator")
'''


from matplotlib import pyplot 
title = 'math and english'
x = [67, 88, 78, 75, 60]

y = (98, 80, 85, 89, 93)
pyplot.plot(title)
pyplot.plot(x, y)

pyplot.show()