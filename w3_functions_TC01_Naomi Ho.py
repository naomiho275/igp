#####  Store your, name, email, student_id and class_number as STRINGS #####
#exercise = "functions and loops"
#name = "Naomi Ho Ai Hui"
#np_email = "s10242585@connect.np.edu.sg"
#student_id = "S10242585D"
#class_number = "TC01"

#-------------------------------- Q1 ------------------------------------#
# Write a program that allow users to calculate distance, time, speed.
#------------------------------------------------------------------------#

# The program should include 3 functions:

    #### speed_function() ####
    # speed = distance/time

    #### distance_function() ####
    # distance = time * speed

    #### time_function() ####
    # time = distance/speed

# The functions will round float to 2 decimal places.

# When the 3 functions are executed, they should display and return:

    ##### Example of speed_function() #####
    ## Enter distance (in km): 10
    ## Enter time taken (in hours): 2
    ## Based on the distance and time input, the calculated speed (km/hr) = 5.0
    
    ##### Example of distance_function() #####
    ## Enter time taken (in hr): 2
    ## Enter speed (in km/hr): 5
    ## Based on the speed and time input, the calculated distance (km) =  10.0

    ##### Example of time_function() #####
    ## Enter distance (in km): 10
    ## Enter speed (in km/hr): 5
    ## Based on the speed and distance input, time taken (in hr) = 2.0

# Using def to create a function 
def speed_function():
    """
    - Function calculates speed based on input of distance and time
    """
    # Asking the user to input the distance and using float function to change the inputed number from str to float
    distance= float(input("Enter distance (in km): "))
    # Asking the user to input the time and using float function to chnage the inputed number from str to float
    time = float(input(" Enter time (in hr): "))
    # Using the inputed number to calculate the speed, and rounding it to 2 decimal places using round function 
    speed= round(distance/time,2)
    # Using return keyword so that the function will give back the calculated value of speed in the main program
    return speed 
# Print the final answer of speed 
print(f"Based on the distance and time input, the speed (in km/hr) = {speed_function()}")


#  Using def to create a function 
def distance_function():
    """
    - Function calculates distance based on input of speed and time
    """
    # Asking the user to input the time and using float function to change the inputed number from str to float
    time= float(input("Enter time taken (in hr) : "))
    # Asking the user to input the speed and using float function to change the inputed number from str to flaot 
    speed= float(input("Enter speed (in km/hr) : "))
    # Using the inputed numbers to calculate distance using the formula and rounding it to 2 decimal places using the rounf function
    distance= round(time*speed,2)
    # Using return keyword so that the function will give back the calculated value of speed in the main program
    return distance 
# Print the final answer of distance 
print(f"Based on the time and speed input, the calculated distance (in km) = {distance_function()}")


#  Using def to create a function 
def time_function():
    """
    - Function calculates time taken based on input of distance and speed
    """
    #  Asking the user to input the distance and using float function to change the inputed number from str to float
    distance= float(input("Enter distance (in km): "))
    # Asking the user to input the speed and using float function to change the inputed number from str to float
    speed= float(input("Enter speed (in km/hr): "))
    # Using the inputed numbers to calculate the time using the formula and rounding it to 2 decimal places using the round function
    time= round(distance/speed,2)
    # Using return keyword so that the function will give back the calculated value of speed in the main program
    return time 
# Print the final answer of distance 
print(f"Based on the distance and speed input, the calculated time (in hr) = {time_function()}")


