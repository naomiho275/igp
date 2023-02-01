# 1. Create 2 string variables `firstname`, `lastname` with 
# your own name first and last name.
firstname = "naomi"
lastname = "ho"
print(firstname)
print(lastname)
# 2. Combine the `firstname`, `lastname` variabls as `fullname`
# with `+` and put a whitespsace with a quotation " " 
# between the  firstname and lastname.
firstname = "naomi"
lastname = "ho"
fullname = firstname + " " + lastname
print(fullname)
# 3. Print the length of "fullname".
print(len(fullname))
# 4. Print the word "financial" from "financial_management" 
# with the slice notation [].
title = "financial_management"
print(title[0:9])
# 5. Print each word in the "sentence" variable on a separate line using `\n`.
sentence = "statistics economics programming"
print("statistics \neconomics \nprogramming ")
# 6. Check if the 2 variables below are equal. It should return 
# a boolean: True or False.
module_1 = "marketing"
module_2 = "accounting"
print("module_1" == "module_2")
# 7.
# Check the length of `country` variable.
# Remove any unwanted whitespace and and assign 
# to a new variable named `country_strip`.
# Check the length of `country_strip`.
country = ("      this is our country: Singapore  ")
print(len(country))
print(country.strip())
country_strip = country.strip()
print(len(country_strip))
# 8. Use formatted strings  f"{}" to print the address variables below:

block = "50"
unit = "20-22"
street = "clementi road" 
postal_code = "573679"

print(f"{block} {unit} {street} {postal_code}")
# 9. Use `.replace()` to replace `Rihana` to `BTS` in `favourite_artist` variable.
favourite_artist = "Rihana is my favourite artist"

print(favourite_artist.replace("Rihana", "BTS"))
# 10.  
# Ask a user's for his/her favourite colour and print the number of characters of the colour.
# Example:
# What is your favorite colour? (suppose the user enter "hotpink")
# Your favorite colour contains 7 characters.

favouritecolour = input ("What is your favourite colour :")
print(favouritecolour)
print(len(favouritecolour))

### Remember to "Run Python File" instead of "Run Code" when using input function.

# 11. 
# Ask a user's for his/her favorite book and print the title from lowercase to uppercase.
# Example:
# What is your favorite book? (suppose the user enter "little red riding hood")
# Your favorite book is LITTLE RED RIDING HOOD

favouritebook = input ("What is your favourite book :")
print(favouritebook.upper())
### Remember to "Run Python File" instead of "Run Code" when using input function.
