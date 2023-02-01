# write a loop to produce the square table 
x=1
while x<=10:
     print(f" square of {x} is {x**2}")
     x=x+1

# comparison operators != (not equal to comparison operator), < (less than operator)
print(5!=6) # the result will only return true or false when using the comparison operators

# Addition assignment operator += (adds the two values and assigns the result back to a variable)
number= 0
number += 1 # this is essentially saying number = number + 1 and so on for lines 14 & 15
number += 2
number += 3
print(number)

# while loop
number = 1
while number < 5 :
     print(number)
     number += 1

set_password = "I love python"
user_input= input(" enter your user password : ")

while set_password != user_input: 
     user_input= input("invalid password! Enter your user password: ")

print("welcome back")

# for loop
for letter in ("singapore") : 
     print(letter)

for letter in enumerate ("singapore") : 
     print(letter)
# enumerate only works on iterable objects ( numbers are not iterable )

#for number in 12345: 
     #print(number)
# there will be an error and enumerate function will not work as well as it is not iterable

for index, letter in enumerate ("singapore"):
     print(f" count {index} character {letter}")

for number in range(1,6): 
     print(number)

for number in range(1,100,10):
     print(number)

def loop(upperlimit):
 num=1
 while num<= upperlimit:
     print(f"double of loop {num} is {num*2}")
     num += 1
loop(upperlimit=9) 
loop(upperlimit=100)

def loop(upperlimit,times):
     num=1
     while num <= upperlimit:
          print(f"Double of loop {num} is {num*times}")
          num+=1

upperlimit=int(input("Please enter an upper limit greater than 1: "))
times=int(input("Please enter a number for multiplication: "))
loop(upperlimit,times)


