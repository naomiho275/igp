#####  Store your name, email, student_id and class_number as STRINGS #####
ind_assign1 = "day 1"
name = "Naomi Ho Ai Hui"
np_email = "s10242585@connect.np.edu.sg"
student_id = "S10242585D"
class_number = "TC01"

# PUT YOUR CODE SOLUTIONS FOR BOTH QUESTIONS INTO ONE PYTHON FILE.
# DON'T NEED TWO SEPARATE PYTHON FILES FOR TWO QUESTIONS. 
# SEPARATE THE CODES WELL BETWEEN QUESTIOS 
# REMEMBER TO INCLUDE COMMENTS TO EXPLAIN YOUR CODE.

#Question 1:

# creating a function to calculate the average acceleration 
def acceleration_function(final_velocity,starting_velocity,elapsed_time ):
    """
    -Function accepts three parameters, final velocity, starting velocity, and elapsed time 
    -Function calculates the average acceleration based on the final velocity, starting velocity, and elapsed time
    """
    # using the formula to calculate the average acceleration 
    average_acceleration= (final_velocity-starting_velocity)/elapsed_time
    # return the calculated average acceleration into the main program and rounding the average acceleration calculated to 2 decimal places 
    return f"Drone acceleration = {round(average_acceleration,2)} meters per second"
# print the function with the respective parameter values inputted by user 
print(acceleration_function(25,6,8))



# Question 2: 

# creating a function to check if the password is weak or strong
def check_pw(password):
    """
    - Function will accept one parameter 
    - Function is to check if the password is weak or strong
    """
    # using while true to create an infinite loop
    while True:
        # using if to see if the password length is more than or equal to 14 
        if len(password)>=14:
            # using for loop to see if the alphabet in the password is uppercase or not 
            for a in str(password):
                if a.isupper() == True:
                    print("Strong Password") 
                    # using break to stop the code when the character is in uppercase
                    break
                # using elif to see if the alphabet in the password is uppercase or lowercase
                elif 'b' in str(password):
                    if 'b'.isupper()== True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                     break
                # using elif to see if the alphabet in the password is uppercase or not
                elif 'c' in str(password):
                    if 'c'.isupper()==True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                     break
                # using elif to see if the alphabet in the password is uppercase or not
                elif 'd' in str(password):
                    if 'd'.isupper()==True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                     break
                # using elif to see if the alphabet in the password is uppercase or not
                elif 'e' in str(password):
                    if 'e'.isupper()==True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                     break
                # using elif to see if the alphabet in the password is uppercase or not
                elif 'f' in str(password):
                    if 'f'.isupper()==True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                     break
                # using elif to see if the alphabet in the password is uppercase or not
                elif 'g' in str(password):
                    if 'g'.isupper()==True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                     break
                # using elif to see if the alphabet in the password is uppercase or not
                elif 'h' in str(password):
                    if 'h'.isupper()==True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                     break
                # using elif to see if the alphabet in the password is uppercase or not
                elif 'i' in str(password):
                    if 'i'.isupper()==True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                    break
                # using elif to see if the alphabet in the password is uppercase or not
                elif 'j' in str(password):
                    if 'j'.isupper()==True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                     break
                # using elif to see if the alphabet in the password is uppercase or not
                elif 'k' in str(password):
                    if 'k'.isupper()==True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                     break
                # using elif to see if the alphabet in the password is uppercase or not
                elif 'l' in str(password):
                    if 'l'.isupper()==True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                     break
                # using elif to see if the alphabet in the password is uppercase or not
                elif 'm' in str(password):
                    if 'm'.isupper()==True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                     break
                # using elif to see if the alphabet in the password is uppercase or not
                elif 'n' in str(password):
                    if 'n'.isupper()==True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                     break
                # using elif to see if the alphabet in the password is uppercase or not
                elif 'o' in str(password):
                    if 'o'.isupper()==True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                     break
                # using elif to see if the alphabet in the password is uppercase or not
                elif 'p' in str(password):
                    if 'p'.isupper()==True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                     break
                # using elif to see if the alphabet in the password is uppercase or not
                elif 'q' in str(password):
                    if 'q'.isupper()==True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                     break
                # using elif to see if the alphabet in the password is uppercase or not
                elif 'r' in str(password):
                    if 'r'.isupper()==True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                     break
                # using elif to see if the alphabet in the password is uppercase or not
                elif 's' in str(password):
                    if 's'.isupper()==True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                     break
                # using elif to see if the alphabet in the password is uppercase or not
                elif 't' in str(password):
                    if 't'.isupper()==True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                     break
                # using elif to see if the alphabet in the password is uppercase or not
                elif 'u' in str(password):
                    if 'u'.isupper()==True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                     break
                # using elif to see if the alphabet in the password is uppercase or not
                elif 'v' in str(password):
                    if 'v'.isupper()==True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                     break
                # using elif to see if the alphabet in the password is uppercase or not
                elif 'w' in str(password):
                    if 'w'.isupper()==True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                     break
                # using elif to see if the alphabet in the password is uppercase or not
                elif 'x' in str(password):
                    if 'x'.isupper()==True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                    #  break
                # using elif to see if the alphabet in the password is uppercase or not
                elif 'y' in str(password):
                    if 'y'.isupper()==True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                    break
                # using elif to see if the alphabet in the password is uppercase or not
                elif 'z' in str(password):
                    if 'z'.isupper()==True:
                     print("Strong Password")
                    else:
                     print("Weak Password")
                    # using break to stop the code when the character is in uppercase
                    break   
        # using else to see if the length of the password is less than 14 characters and return weak password if it is less than 14
        else:
            print("Weak Password")
        # using break to stop the code when the length of the code is less than 14 characters 
        break
# calling out the check_pw(password) code
check_pw("NgeeannPolytechniC")

            

