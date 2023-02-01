#####  Store your, name, email, student_id and class_number as STRINGS #####
#exercise = "numbers"
#name = "Naomi Ho Ai Hui"
#np_email = "s10242585@connect.np.edu.sg"
#student_id = "S10242585D"
#class_number = "TC01"

#-------------------------------- Q1 ----------------------------------------#
# Write a program to ask user to input two numbers using 2 input functions.    
# The program will check if the sum between these 2 numbers is an integer. 
#----------------------------------------------------------------------------#

#Asking user to input the first number 
num1= input("Enter first number: ")
#Converting the inputed num1 from a string to a float
num1=float(num1)
#Asking user to input the second number 
num2= input("Enter second number: ")
#Converting the inputed num2 from a string to a float
num2=float(num2)
#Assigning the sum of num1 and num2 to the variable sum_num
sum_num=num1+num2
#Print the sum of num1 and num2 
print(sum_num)
# Using is.integer() to check if the sum of num1 and num2, sum_num, is an integer or not
print(f"Is the sum of num1 and num2 an integer?{sum_num.is_integer()}")

# The program should display message like the following when executed.

    #------ First execution ------#
    # Enter first number : 3.5
    # Enter second number : 1.5
    # 3.5 + 1.5 = 5.0
    # Is the sum of 3.5 and 1.5 an integer? True

    #------ Second execution ------#
    # Enter first number : 3.5
    # Enter second number : 2.3
    # 3.5 + 2.3 = 5.8
    # Is the sum of 3.5 and 2.3 an integer? False

# In the first execution, the input values are  3.5 and 1.5
# In the second execution, the input values are 3.5 and 2.3
# The program will sum the 2 numbers and return True when the sum is an integer or False when sum is a float.

# Assign `num1` as a variable for the first number, `num2` as a variable for the second number
# Assign `sum_num` as the variable to store the arithmatic operation between `num1` and `num2`  



#-------------------------------- Q2 ----------------------------------------#
# Write a program to ask user to input two numbers using 2 input functions.  
# The program will use the first number as dividend and second number as a divisor.
# The output should return the remainder of the division. 
#----------------------------------------------------------------------------#

#Asking the user to input a number which will be the dividend 
num3=input("Enter a dividend: ")
#Converting the num3 inputed by the user from a string to a float 
num3=float(num3)
#Asking the user to input a number which will be the divisor 
num4= input("Enter a divisor: ")
#Converting the num4 inputed by the user from a string to a float 
num4=float(num4)
#Using the modulus operator to find out the remainder of num3 divided by num4 and assiging it to the variable modulus 
modulus=num3%num4
#Print the remainder of num3 divided by num4
print(f"The remainder is {modulus}")

# The program should display the following messages :

    # Enter a dividend: 30
    # Enter a divisor: 3
    # The remainder is 0.0

# In the execution above, the input values are  30  and 3. The program will return the remainder of 30 divided 3.

# Assign `num3` for the dividend and `num4` for the divisor.
# Assign 'modulus` to store the results of the operation.