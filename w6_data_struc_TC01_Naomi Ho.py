#####  Store your, name, email, student_id and class_number as STRINGS #####
#exercise = "Data Structure"
#name = "Naomi Ho Ai Hui"
#np_email = "s10242585@connect.np.edu.sg"
#student_id = "S10242585D"
#class_number = "TC01"

#--------------------- 1. List ---------------------#

# You are given information of the membership numbers and the membership fees of the local gyms.
# The information is a nested list `gym_data`. The elements in each sub-list contain:
## 1. The gym name
## 2. The number of members
## 3. Membership fee per member

gym_data_list = [['FitFirst', 8500, 3500], ['PlanetFit', 5500, 2300], [
    'GoldGym', 9000, 1800], ['AnyTimeFit', 7200, 2400], ['VirginFit', 3200, 3800]]

# 1.
# Write a function `total_summary_list` with a single parameter `option`.
# When "membership" is supplied to the option parameter, `total_summary_list` function will return
# the total number of membership across the gyms.
# When "fee" is supplied to the option parameter, `total_summary_list` function will return
# the total membership fee revenue collected across the gyms.
# Otherwise, it will return `invalid entry` for any other values supplied to the `option` parameter.
# Note: total membership fee revenue =  the number of members x membership fee per member

# Creating a function to return either total number or membership or the total membership fee revenue across the gyms
def total_summary_list(option):
    """
    - This function will return the total membership across the gyms
    - This function will return the total membership fee revenue across the gyms 
    - This function accepts a single parameter 
    """
    # Create a variable and assign the value of 0
    total = 0 
    # checking if the value supplied to the 'option' variable is "membership"
    if option == "membership": 
        # using a for loop to loop the data from the gym_data_list
        for data in gym_data_list: 
            # Calculating the total number of members 
            total += data[1] 
            # assigning the statement of total membership across the gyms to the variable of statement 
            statement = f"Total number of members across the gyms: {total}"    
    # checking if the value supplied to the 'option' parameter is "fee"
    elif option == "fee" : 
        # using a for loop to loop the data from the gym_data_list
        for data in gym_data_list: 
            # calculating the total membership fees revenue 
            total += data[1]*data[2]
            # assigning the statement of total membership fees revenue across the gyms to the variable of statement
            statement = f"Total membership fees revenue collected across the gyms: ${total}"
    # checking if other values other than "membership" or "fee" are supplied to the 'option' variable 
    else: 
        # assigning the statement of "Invalid Entry" to the variable statement
        statement = "Invalid Entry"
    # return the statement to the main program 
    return statement

print(total_summary_list("membership"))
print(total_summary_list("fee"))


# Examples of what the functions will display and return when executed:

## print(total_summary_list("membership"))
## Total number of members across the gyms: 33400


## print(total_summary_list("fee"))
## Total membership fees revenue collected across the gyms: $88040000

#--------------------- 2. Dictionary ---------------------#
# The same information is now structured as a dictionary.
# Write a similar function that will total number of membership and
# total membership fee revenue.

gym_data_dict = {'FitFirst': {"number of members": 8500,
                              "membership fee": 3500
                              },
                 "PlanetFit": {"number of members": 5500,
                               "membership fee": 2300
                               },
                 "GoldGym":  {"number of members": 9000,
                              "membership fee": 1800
                              },
                 "AnyTimeFit": {"number of members": 7200,
                                "membership fee": 2400
                                },
                 "VirginFit": {"number of members": 3200,
                               "membership fee": 3800
                               },
                 }

# creating a function to return either total number or membership or the total membership fee revenue across the gyms using the gym_data_dict
def total_summary_dict(option):
    """
    - This function will return the total membership across the gyms
    - This function will return the total membership fee revenue across the gyms 
    - This function accepts a single parameter 
    """
    # Creating a variable and assigning the value of 0
    total = 0
    # checking if the 'option' parameter supplied is "membership"
    if option == "membership": 
        # creating a for loop to loop the data from the dictionary 
        for member,fee in gym_data_dict.items(): 
            # calculating the total membership across gyms using "number of members" found in the dictionary
            total += gym_data_dict[member]["number of members"]
            # Assigning the statement of total number of members across the gym to the variable statement 
            statement = f"Total number of members across the gyms: {total}"
    # checking if the 'option' parameter supplied is "fee"
    elif option == "fee": 
        # creating a for loop to loop the data from the dictionary 
        for member,fee in gym_data_dict.items():
            # calculating the total membership fees revenue across gyms using "membership fees" found in the dictionary
            total += gym_data_dict[member]["number of members"] * gym_data_dict[member]["membership fee"]
            # Assigning the statement of total membership fees revenue to the variable statement 
            statement = f"Total membership fees revenue collected across the gyms: ${total}"
    # checking if other values other than "membership" or "fee" are supplied to the 'option' variable 
    else: 
        # Assigning the statement of "Invalid Entry" to the variable statement 
        statement = "Invalid Entry"
    # returning the statement to the main program 
    return statement
    
print(total_summary_dict("membership"))
print(total_summary_dict("fee"))


# Examples of the functions when executed:

    ## print(total_summary_dict("membership"))
    ## Total number of members across the gyms: 33400

    ## print(total_summary_dict("fee"))
    ## Total membership fees revenue collected across the gyms: $88040000
