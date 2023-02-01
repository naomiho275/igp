#comparison operators in python: <, >, <=, >=, !=, == 
print (2<3) # the return will be true since 2 is less than 3 (< symbol is less than)
print(2>3) # the return will be false since 2 is NOT more than 3 (> symbol is greater than)
print(3>=3) # the return will be true because 3 is equal to 3, even though 3 is not greater than 3 
print(3<=3) # the return will be true because 3 equal to 3, even though 3 is not lesser than 3 
print (1==True) # the return will be true since true assumes the value of 1 
print(0==False) # the return will be true since false assumes the value of 0 

#Comparing strings : 
print("a" < "b") # the return will be true (a has a lower order than b)
print("c" < "b") # the return will be false (b has a lower order than c)
# this is due to the order of a-z 

# An Example: 
set_pw="tgif"
print(set_pw=="tgip") # the return will be false 

print(set_pw <= "tgip") # the return will be true as the alphabet p is a higher order than f 

# Logical Operators : and, or, not 

num1=200
print(num1 > 150 and num1 < 250) # the return will be true 
# the and operator will require both the conditions on the left and right to return true in order to evaluate an overall true
# if either condition is false, the return will be false as only one returns a true and the other returns a false

print(num1 < 150 or num1 > 250 ) # the return will be true 
# the or operator only requires one of the condition to be true in order for the return to be true 

print(not True ) # the return will be false since not true means false 
print (not False) # the return will be true since not false means true 
print( not False==1) # return will be true since true = 1 

# Operator Precedence: determines which operator will be executed first when more than one operator is used 
# A parenthesis could be used to set execution order 
# The statements in the parenthesis are evaluated first 
# without the parenthesis there will be a syntax error 
# Example: 
print(1==(not 1))

# if and else statement : 
language = "python"

if language != "python": 
    print(f"Programming language is {language}") # return will be false 

singtel = 1.3
starhub=1.8
if singtel > starhub: 
    print("Singtel price is higher than Starhub")
else : 
    print("Starhub price is higher than Singtel")

# elif keyword 
singtel = 1.3
starhub=1.8
if singtel > starhub: 
    print("Singtel price is higher than Starhub")
elif singtel < starhub: 
    print("Starhub price is higher than Singtel")
elif singtel == starhub: 
    print("Share prices are equal")

# conditions and loops 
even_sum = 0
odd_sum = 0 

for num in range (10):
    if num % 2 == 0 : 
        even_sum += num
    else : odd_sum += num
print(f"Even sum of 0 to 9 = {even_sum}")
# sum of 0, 2, 4, 6, 8 
print(f"Odd sum of 0 to 9 = {odd_sum}")
# sum of 1, 3, 5, 7, 9

# break keyword ( to stop an iteration ):
range_value= range(50,100)

for index, num in enumerate(range_value):
    print(index,num)
    if index == 5 :
        break # the loop will stop at index 5 because of the break keyword (without the keyword, it will stop at num 99)

# continue keyword (to skip an interation):

for num in range (10):
    if num==5 or num==6 :
        continue 
    print(num)
# the number of 5 and 6 are skipped and not printed because of the continue keyword









