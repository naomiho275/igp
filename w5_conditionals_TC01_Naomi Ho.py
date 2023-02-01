#####  Store your, name, email, student_id and class_number as STRINGS #####
#exercise = "conditionals"
#name = "Naomi Ho Ai Hui"
#np_email = "s10242585@connect.np.edu.sg"
#student_id = "S10242585D"
#class_number = "TC01"

#------------------------ Part 1 : if, elif, else ------------------------#
# Write a function: tax_rebate() to determine tax rebate from income level
#-------------------------------------------------------------------------#

# The function will prompt a user to declare his/her yearly income
# and determine the amount of one-time off tax rebate he/she should receive.
# Note that the function does not require any parameters. It will return the
# amount of tax rebate based on the following tax rules:

# Yearly Income in $ 	                # Tax Rebate in $
# ------------------                      -------------
# 0 to less than 40000 	                      2000
# 40000 to less than 100000	                  1000
# 100000 to less than 150000 	              500
# equal or greater than 150000 	             not eligible

# Executing the function based om different income levels will display and return output
# like the followings:

#### Example 1 ####
# Declare your yearly income : 10000
# Your tax rebate is : $2000

#### Example 2 ####
# Declare your yearly income : 80000
# Your tax rebate is : $1000

#### Example 3 ####
# Declare your yearly income : 110000
# Your tax rebate is : $500

#### Example 4 ####
# Declare your yearly income : 150000
# You are not eligible for tax rebate

#### Example 5 ####
# Declare your yearly income : 200000
# You are not eligible for tax rebate

# creating a tax rebate function
def tax_rebate():
    """
    - function will return rebate based on income level
    """
    # asking user to input their yearly income using the input function
    userinput=input("Declare your yearly income:")
    # converting the input from string to float
    userinput=float(userinput)
    # checking if the input is more than or equal to 150000 using if 
    if userinput>=150000:
        # if the users input is more than or equal to 150000, the statement of You are not eligible for tax rebate will be printed
        print("You are not eligible for tax rebate")
    # checking if the input is more than 100000 using elif
    elif userinput >= 100000:
        # if the users input is more than 10000, the statement of Your tax rebate is $500 will be printed
        print("Your tax rebate is $500")
    # checking if the input is more than 40000
    elif userinput >= 40000:
        # if the users input is more than 40000, the statement of your tax rebate is $1000 will be printed
        print("Your tax rebate is $1000")
    # checking if the users input is less than 40000
    else:
        # if the users input is anything less than 40000, the statement of your tax rebate is $2000 will be printed
        print("Your tax rebate is $2000") 
# calling out the tax_rebate() function        
tax_rebate()
        
#---------------------------------- Part 2  ---------------------------------#
# Improve the tax_rebate() function from Part 1 to make the program
# less susceptible to crashing.
#----------------------------------------------------------------------------#

# It should prevent the program from crashing if the user entered "string"
# data type when declaring his/her income.

# The function should loop endlessly to ask the user to declare the income until
# he/she use "number" data type.

# Here is an example of how the program will behave:

    # Declare your yearly income: ten thousand
    # [INVALID INPUT] Only number is accepted, please re-enter again.
    # Declare your yearly income: one thousand
    # [INVALID INPUT] Only number is accepted, please re-enter again.
    # Declare your yearly income: 10000
    # Your tax rebate is : $2000

# Tips:
# Design the function with `while loop` in mind, so that program will
# keep looping until the user input entered the correct data type.

# creating a second tax rebate function 
def tax_rebate_2():
    """
    - Function will return rebate based on income level
    """
    # using while true to create an infinite loop
    while True: 
        # asking the user to input their yearly income 
        userinput=input("Declare your yearly income:")
        # using .isdigit() to make sure that the input is a digit 
        if userinput.isdigit():
            # converting the input from string to float 
            userinput=float(userinput)
            # checking if the input is more than or equal to 150000 using if 
            if userinput>=150000:
                # if the users input is more than or equal to 150000, the statement of You are not eligible for tax rebate will be printed
                print("You are not eligible for tax rebate")
            # checking if the input is more than 100000 using elif
            elif userinput >= 100000:
                # if the users input is more than 100000, the statement of Your tax rebate is $500 will be printed
                print("Your tax rebate is $500")
            # checking if the input is more than 40000 using elif
            elif userinput >= 40000:
                # if the users input is more than 40000, the statement of Your tax rebate is $1000 will be printed
                print("Your tax rebate is $1000")
            # checking if the users input is less than 40000 using else
            else:
                # if the users input is any number below 40000, the statement of Your tax rebate is $2000 will be printed
                print("Your tax rebate is $2000")
                # using break to break the infinite loop after the user has inputted the income and tax rebate is printed 
            break
        # using else to print error message whenever the user's input is not a number or contains a character 
        else:
            print("[INVALID INPUT] Only number is accepted, please re-enter again")  
# calling out the tax_rebate_2() function                    
tax_rebate_2()           



