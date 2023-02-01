#####  Store your, name, email, student_id and class_number as STRINGS #####
#exercise = "loops"
#name = "Naomi Ho Ai Hui"
#np_email = "s10242585@connect.np.edu.sg"
#student_id = "S10242585D"
#class_number = "TC01"

#-------------------------------- Q2 ------------------------------------#
# Write a function: loan_calculator(amount, interest, month).
# The function will calculate the total loan amount payable.
#------------------------------------------------------------------------#

#### Example of how the function works ####

# Given a loan amount of $1000, 10% interest rate and 5 month loan period,
# the function will calculate the interests payment plus the principal loan amount.
# When `loan_calculator(1000,0.10,5)` is executed, it will return $1610.51

# The calculation of $1610.51 is as follow:
# Month 1 = $1100 ($1000 * 1.1)
# Month 2 = $1210 ($1100 * 1.1)
# Month 3 = $1331 ($1210 * 1.1)
# Month 4 = $1464.1 ($1331 * 1.1)
# Month 5 = $1610.51 ($1464 * 1.1)

# Round off decimals to 2 decimal places.
# BONUS: Can you use f-strings to include a $ symbol with the return value?

def loan_calculator(amount, interest, month):
    """
    Describe what the function does and what parameters are required
    """
# using for loop to loop the months entered from 1st month to the number of months entered 
    for month in range(1, month+1):
            # assigning total loan amount to a variable to calculate the amount, convert in to float and using the round function to round the amount to 2 decimal places
            loantotalamount= float(round(amount*(1+interest),2))
            # printing statement of the total amount of each month and the workings to get there 
            print(f'Month {month} = ${loantotalamount} (${amount}*{1+interest})')  
            #using the previous amount as the current amount in the next month's loop 
            amount = loantotalamount
    #Using the print function to print the total amount
    print(f"The total amount is ${loantotalamount}")

loan_calculator(1000,0.10,5)
loan_calculator(5000,0.15,8)