#####  Store your name, email, student_id and class_number as STRINGS #####
ind_assign1 = "day 2"
name = "Naomi Ho Ai Hui"
np_email = "s10242585@connect.np.edu.sg"
student_id = "S10242585D"
class_number = "TC01"

# PUT YOUR CODE SOLUTIONS FOR BOTH QUESTIONS INTO ONE PYTHON FILE.
# DON'T NEED TWO SEPARATE PYTHON FILES FOR TWO QUESTIONS. 
# SEPARATE THE CODES WELL BETWEEN QUESTIOS 
# REMEMBER TO INCLUDE COMMENTS TO EXPLAIN YOUR CODE.

# Question 1:

# creating a function that calculates the waist hip ratio and return the health risk level
def waist_hip():
    """
    - Function has no parameters 
    - Function calculates the Waist to Hip Ratio 
    - Function will use the calculated Waist to Hip ratio and return the accurate health risk level 
    """
    # asking user to input their gender 
    gender= input("What is your gender (M or F)?")
    # asking user to input their waist measurement in inches
    waist= float(input("What is your waist measurement (inches)?"))
    # asking user to input their hip measurement in inches 
    hip= float(input("What is your hip measurement (inches)?"))
    # calculating the waist hip ratio by dividing the waist measurement by the hip measurement using / 
    waist_hip_ratio= waist/hip
    # checking if the waist to hip ratio is more than 1 and if the gender is Male using .upper() to ensure the code can still run if the alphabet is in lower case 
    if waist_hip_ratio >= 1.0 and gender.upper()=="M":
        # printing the health risk statement (High Risk) when the above conditions are met 
        print("Your Health Risk: High Risk")
    # checking if the waist to hip ratio is more than or equal to 0.9 and if the gender is Male using .upper() to ensure the code can still run if the alphabet is in lowercase
    elif waist_hip_ratio >= 0.9 and gender.upper()=="M":
        # printing the health risk statement (Moderate Risk) when the above conditions are met 
        print("Your Health Risk: Moderate Risk")
    # checking if the waist to hip ratio is less than 0.9 and if the gender is Male using .upper() to ensure the code can still run if the alphabet is in lowercase
    elif waist_hip_ratio < 0.9 and gender.upper()=="M":
        # printing the health risk statement (Low Risk) when the above conditions are met 
        print("Your Health Risk: Low Risk")
    # checking if the waist to hip ratio is more than 0.9 and if the gender is Female using .upper() to ensure the code can still run if the alphabet is in lowercase
    elif waist_hip_ratio >=0.9 and gender.upper()== "F" :
        # printing the health risk statement (High Risk) when the above conditions are met
        print("Your Health Risk: High Risk ")
    # checking if the waist to hip ratio is more than or equal to 0.8 and if the gender is Female using .upper() to ensure the code can still run if the alphabet is in lowercase
    elif waist_hip_ratio >=0.8 and gender.upper()=="F":
        # printing the health risk statement (Moderate Risk) when the above conditions are met
        print("Your Health Risk: Moderate Risk")
    # checking if the waist to hip ratio is less than 0.8 and if the gender is Female using .upper() to ensure that the code can still run if the alphabet is in lowercase 
    elif waist_hip_ratio <0.8 and gender.upper()=="F":
        # printing the health risk statement (Low Risk) when the above conditions are met
        print("Your Health Risk: Low Risk")
# calling out the waist to hip ratio function 
waist_hip()


#Question 2:
# creating a function to convert the age in years to age in days 
def calc_age(age):
    """
    - Function accepts one parameter 
    - Function converts the age in years to the age in days 
    """
    # converting the age in years to age in days by multiplying the age in years by 365 using * 
    daysage=age*365
    # checking if the age is a positive number (more than or equal to 0)
    if daysage>=0:
        # printing the statement of Age in years is equal to the age in days 
        print(f"{age} years is equal to {daysage} days")
    # checking if the age is a negative number 
    else:
        # printing the statement that Age cannot be a negative number when the age is negative (less than 0)
        print("Age cannot be a negative number")
# calling out the age calculation function 
calc_age(40)
calc_age(-10)
        
