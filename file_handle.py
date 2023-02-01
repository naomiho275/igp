# Create Path Objects 
from pathlib import Path
# The letter r will switch off backslash as an escape character
file_path= Path(r"C:\Users\naomi ho\python4biz\test.txt.txt")
print(file_path)
# .exists() is to check if the file path exists in the computer -> If it exists the return will be True. If it Does not the return will be false
print(file_path.exists())

# Path.home() : 
# This class method creates a Path object representing the user's home directory 
# Home directory usually refers to C:\Users\John 
# The / operator must always have a path object on the left-hand side 
# The right hand side can have a string representing a single file or directory, or it can have a string representing a path or other path object 
# Path.home() creates a file path pointing to the computer's home directory 
from pathlib import Path
home=Path.home()
print(home)
filepath=home/"python4biz"/"test.txt.txt"
print(filepath)
print(filepath.exists())

# Path.cwd() : 
from pathlib import Path
print(Path.cwd())
fp_cwd= Path.cwd()/"datastructure.py"
print(fp_cwd.exists())

# Stem and Suffix a File name 
# File names are usually broken down into 2 parts 
# The part to the left of the dot (.) is called the stem 
# The part to the right of the dot (.) is called the suffix or the file extension
# Pathlib has 2 attributes .stem and .suffix to retrieve the stem and suffix 
from pathlib import Path
home=Path.home() # This is to instantiate a file path object to home directory 
file_path=home/"python4biz"/"test.txt"
print(f"Stem: {file_path.stem}")
print(f"Suffix: {file_path.suffix}")

# Create a new file with Path.touch() :
from pathlib import Path
home=Path.home()
print(home)
file_path=home/"python4biz"/"contacts.txt"
file_path.touch()
file_path.exists()

# Iterating over Dictionary Contents: 
# iterdir(): 
# Path objects have a .iterdir() for creating an iterator for all the files and folders in directory 
# .is_file() checks if the items in the folder is a file and returns True or False 
# .name is an attribute that returns file name 
from pathlib import Path
home= Path.home()
file_path=home/"python4biz"
for file in file_path.iterdir():
    if file.is_file(): 
        print(file.name)

# .glob() : 
# If a folder consists of different file extension, Path.glob() allows a search of certain type of files through iteration
from pathlib import Path
home=Path.home()
file_path = home/"python4biz"
for file in file_path.glob("*.txt"): 
# * in ("*.txt") acts like a wildcard character which replaces any number of characters before the suffix
# files like new_word.docx will be filtered out in the iteration since search is for filename that consists of .txt only
    print(file)

# Read and Write Text Files:
 
# Read Files : 
# There are 2 ways to create a file object in Python
# 1. The Path.open() method
# 2. The built-in open() function 
# Path.open() : 
# 1. Path.open() returns a file object 
# 2. mode = "r" arguments open a file in 'read mode'
# 3. The encoding parameter determines the character encoding used to decode the file
# The argument UTF-8 represents UTF-8 character encoding
from pathlib import Path

file_path=Path.home()/"python4biz"/"test.txt.txt"

file=file_path.open(mode="r", encoding="UTF-8")

file.close()

# with Statement: 
#  The with statement is used in exception handling to make the code cleaner and more readable 
# It includes a header and a body 
# The header starts with the with keyword and ends with a colon : 
# The return value of path.open() is assigned to the variable name afyer the as keyword
# For example: 
# with file_path.open(mode="r") as file: 

# .read() : 
# .read() method is associated with a text file. It reads the text in the file and returns it as a string 
# If there are multiple lines of text in the file, then each line in the string is separated with a newline character \n

from pathlib import Path

file_path=Path.home()/"python4biz"/"test.txt.txt"

with file_path.open(mode="r", encoding="UTF-8") as file:
    text=file.read()

print(text)

# .readlines():
from pathlib import Path

file_path=Path.home()/"python4biz"/"test.txt.txt"

with file_path.open(mode="r", encoding="UTF-8") as file:
    for line in file.readlines(): 
        print(line) # there will be an extra empty line between each line of text
        print(line, end="") # this is so that no extra new lines are returned

# Write text with write() :
# .write() method writes data into a plain text file 
# To write, "w" needs to be placed in the mode parameter in the open method 
from pathlib import Path
file_path = Path.home()/"python4biz"/"contacts.txt"
with file_path.open(mode="w", encoding="UTF-8") as file:
    file.write("Name: John\nAge: 19")

# Appending Lines:
# Append will always add data to the last line
from pathlib import Path
file_path = Path.home()/"python4biz"/"contacts.txt"
with file_path.open(mode="a", encoding="UTF-8") as file:
    file.write("\nGender: Male")

# Writing Multiple Lines: 
from pathlib import Path
# placing "\n" individually before each data is so that they are written on separate lines instead of all on one line
new_data= ["\n", "Weight: 78","\n" "Height: 176"]

file_path = Path.home()/"python4biz"/"contacts.txt"
with file_path.open(mode="a", encoding="UTF-8") as file:
    file.writelines(new_data)

# Read and write CSV Files: 
# A CSV file is a type of plain text file that uses specific structuring to arrange tabular data
# Example: 
# Counter, open price, closing price, max price -> Everything is separated by a comma
# Usually, the first line identifies each piece of data, in other words, the name of a data column
# Every subsequent line after that is actual dataand is limited only by file size contraints 
# The separator character is called a delimiter, and the comma is not the only one used
# Other popular delimiters include the tab /t, colon :, and semi colon ; characters 

# Purpose of CSV: 
# Reading and writing CSV file is largely similar to simple text files, with additional steps to import a csv module and instantiate CSV objects for reading and writing data into CSV file
# csv.write(): includes .writerow() for writing single line and .writerows() for writing multiple lines 
# csv.read(): allows the retrieval of lines in the csv file 

# csv.write():
from pathlib import Path
import csv 
file_path=Path.home()/"python4biz"/"dbs_shares.csv"
file_path.touch()
print(file_path.exists())

dbs_shares_price=[[1,12.32,11.2], [2,12.31,11.5],[3,12.42,11.6],[4,12.52,11.7],[5,12.32,12.85]]

with file_path.open(mode="w", encoding="UTF-8", newline="") as file: 
    writer=csv.writer(file)
    writer.writerow(["Day", "Opening_Price", "Closing_Price"])
    for sublist in dbs_shares_price:
        writer.writerow(sublist)
# Using .writerows() :
from pathlib import Path
import csv 
file_path=Path.home()/"python4biz"/"dbs_shares.csv"
file_path.touch()
print(file_path.exists())

dbs_shares_price=[[1,12.32,11.2], [2,12.31,11.5],[3,12.42,11.6],[4,12.52,11.7],[5,12.32,12.85]]

with file_path.open(mode="w", encoding="UTF-8", newline="") as file: 
    writer=csv.writer(file)
    writer.writerow(["Day", "Opening_Price", "Closing_Price"])
    writer.writerows(dbs_shares_price)

# csv.reader():
from pathlib import Path
import csv 
file_path= Path.home()/"python4biz"/"dbs_shares.csv"
with file_path.open("r", encoding="UTF-8", newline="") as file:
    reader=csv.reader(file)
    for line in reader:
        print(line)

# next() function:
# This function is used to skip an iteration
from pathlib import Path
import csv 
file_path= Path.home()/"python4biz"/"dbs_shares.csv"
with file_path.open("r", encoding="UTF-8", newline="") as file:
    reader=csv.reader(file)
    next(reader)
    for line in dbs_shares_price: 
        print(line)

# num=[1,2,3,4,5]
# next(num)
# There will be a TypeError 
# next function only works with objects like reader object and does not work with an iterable object like a list, tuple, or dictionary'
# There is a difference between an iterable and iterator 

# Append Values from csv File: 
from pathlib import Path
import csv 
empty_list=[]

file_path= Path.home()/"python4biz"/"dbs_shares.csv"
with file_path.open("r", encoding="UTF-8", newline="") as file:
    reader=csv.reader(file)
    next(reader)
    for line in dbs_shares_price: 
        print(line)
        for value in line: 
            empty_list.append(value)
print(empty_list) # All the values will be contained in a single list and each of the value returned is a string 


