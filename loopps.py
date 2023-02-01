def loan_calculator(amount, interest, month):
    """
    Describe what the function does and what parameters are required
    """
# using for loop to loop the months entered from 1st month to the number of months entered 
    while month+1 > 1 :
            # total loan and convert in to float and using the round function to round the amount to 2 decimal places
            loantotalamount= float(round(amount*(1+interest),2))
            # printing statement of the amount of each month 
            print(f'Month {month} = ${loantotalamount} (${amount}*{1+interest})')  
            #using the previous amount as the current amount in the next month's loop 
            amount = loantotalamount
    #Using the print function to print the total amount
    print(f"The total amount is ${loantotalamount}")

loan_calculator(1000,0.10,5)
loan_calculator(5000,0.15,8)