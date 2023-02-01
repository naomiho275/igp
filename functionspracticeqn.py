def greet():
    greeting="goodmorning!"
    return greeting
print(greet())

def greet():
    print('Good Morning!')
    return 'Good Morning!'


def greetname(your_name):
    print(f"Goodmorning, {your_name}")
your_name=input("Please input your name: ")
greetname(your_name)

def bmi(weight, height):
    result=weight/(height**2)
    return result 
height=float(input("Please enter your height: "))
weight=float(input("Please enter your weight: "))
urbmi= bmi(weight,height)
print(f"With height {height}, weight is {weight}, your bmi is {urbmi}")
if urbmi>22:
    print(f"You are overweight")


#function calculates speed based on input of distance and time


