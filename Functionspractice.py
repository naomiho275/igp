## Functions in Python:

import math
# When we use import math, we importing the whole math library which allows us to use all the functions under it

print(math.ceil(7.1))
# ceil is ceiling and it rounds the number up to the next whole number 

from math import ceil
# By doing this, we will only be importing the ceiling function from math library
print(ceil(7.1))
# Because we only imported ceil, we do not have to put math. in fron like in line 5 anymore

import math
print(dir(math))
# By doing this, all the functions under the math library will be listed out

## Documentation of a Function: 
address_1='150'
address_2='Clementi'
address_3='Singapore'
print(address_1,address_2, sep='-')
# By including sep='-' we change the whitespace between address 1 and 2 from an empty space to a dash 

print(address_1,address_2, end='\t')
print(address_3)
# By using end='\t' python will print address 3 on the same line as address 1 & 2 instead of on a new line

help(print)
#By using help(), we are able to see the documentation exactly like the pop up

## Customised Funtions: 
# SOME RULES: 
# start with a def keyword 
# Provide a name for the function 
# a set of parenthesis and colon (): 
# optional parameters within the parenthesis 
# A body of code to serve the purpose of the function

# convert Metre to Km Example: 
# convert distance units from metre to km (metre x 0.001)
def convertMetretoKM(metre):
    return metre*0.001
print(convertMetretoKM(metre=10000))
# If we did not include the return keyword in line 43, the function will do the multiplication but will not give back the value into main program 
 # For example: 
# def convertMetretoKM(metre):
#     metre*0.001
# print(convertMetretoKM(metre=10000))
# The output for the one without return will be 'none' 

# Another way to use the function:
km= convertMetretoKM(metre=10000)
print(km)

# Docstrings:
def convertMetretoKM(metre):
    """
    - This function converts metre to kilometre
    - one parameter required: metre (as integer or float)
    """
    return metre*0.001
# Anything that is between the two """ quotations, python will assume that as a kind of command

#Function with 2 Parameters: 
def bmi(weight, height):
    """
    - This function calculates BMI with weight and height
    - Two parameters required: weight(in kilograms), height(in metres)
    """
    return weight / height ** 2

print(bmi(68,1.78))

my_bmi= round(bmi(68,1.78),2)
print(my_bmi)

# Scope in Programming: 
# when the vairbale is created outside of a function, that variable is created in the region of a gloabl scope
# The variable that exists outside the variable is called the global variable 
# Local scope (It is where x,y,z exist):
def add():
    x=10
    y=20
    z=x+y
    return z
# x,y,z are variables inside the function
# Variables inside a function is also called local variables
# Local variables only exist within the function
# We are not able to print variables x,y,z individually outside of this function (NameError)
print(add())
# python follows a search order of LEGB
# LEGB ( Local -> Enclosing -> Global -> Built-in) Search order

def accumulate(x):
    y=0
    y=y+x
    return y 

print(accumulate(1))
# In this situation, y is in the local scope. 
# Situation 2 : y in the global scope( hence, y will never reset whenever we use the accumulate funcion )
# y=0
# def accumulate(x):
#     y=y+x
#     return y 
# print(accumulate(1))
# print(accumulate(1))
# Here, there will be an unbound error 

# To overcome this error: 
y=0
def accumulate(x):
    global y 
    y=y+x
    return y 
print(accumulate(1))
print(accumulate(1))
print(accumulate(2))

