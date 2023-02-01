#####  Store your, name, email, student_id and class_number as STRINGS #####
#exercise = "strings"
#name = "Naomi Ho Ai Hui"
#np_email = "s10242585@connect.np.edu.sg"
#student_id = "S10242585D"
#class_number = "TC01"

# ---------- Write a program to allow a user to enter some text ----------#

# The program will:
    # 1. Convert any uppercase strings to lowercase strings.
    # 2. After step 1, it will replace lowercase character of z, b, t, g, h with 1, 2, 3, 4, 5 respectively.

# When your program file is executed, it will look like this:

    # Enter some text in uppercase: I LOVE SINGAPORE ZOO BEST
    # Converted your text to lower case: i love singapore zoo best
    # Replaced any character of z, b, t, g, h with 1, 2, 3, 4, 5: i love sin4apore 1oo 2es3

# You should assign a variable and named it as `text` to store the user input.

# Note:
# `I LOVE SINGAPORE` is the user input text.
# `i love singapore` and `i love sin4apore` are the output of the program

text= input("Please enter some text in uppercase: ")
print(f"Converted your text to: {text.lower()}")
text=text.lower()
text=text.replace("z","1")
text=text.replace("b","2")
text=text.replace("t","3")
text=text.replace("g","4")
text=text.replace("h","5")
print(f"Replaced any character of z,b,t,g,h with 1,2,3,4,5 : {text}")



