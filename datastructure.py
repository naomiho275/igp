# there are three types of data structure in python: Tuple, list, dictionary 
# a data structure is a collection of data such as a list of numbers, a set of strings, or a combination of both 
# Data structure allows more than a single number and a string to be stored -> allows data to be handled more efficently

# Lists: 
# A list is created with a pair of square brackets [] and it can store strings and numbers just like a tuple
# Lists are mutable objects (unlike tuples) which means the values in the list can be changed after creating them
# Example: 
list_nation = ["Singapore", "Malaysia", "Indonesia", "Thailand"]
print(list_nation)
print(list_nation[0]) # This will give a return of Singapore since it is in the position of 0 in the list 
print(list_nation[0:3]) # This will give a return of Singapore Malaysia and Indonesia 

# Lists from Strings: 
# Sometimes we may have to split a long string of items into individual items 
# In order to do so, we can user .split() to split a long string into individual items 
# Each individual item is stored as in list and allows us to retrieve an item in a list easier 
# Example: 
string_countries= "Singapore, Malaysia, Indonesia, Thailand"
print(string_countries)
# Use .split() to separate the countries as individual items 
countries = string_countries.split(",")
print(countries)
# A list allows a for loop to extract items 
for country in countries: 
    if country == "Singapore": 
        print(country)

# Lists are mutable 
# The values in a list are allowed to be replaced or changed 
# Example:
list_nation = ["Singapore", "Malaysia", "Indonesia", "Thailand"]
list_nation[2] = "Laos" # the number 2 is for the position of the string Indonesia 
print(list_nation)
# To change more than a single value : 
list_nation[1:4] = ["Canada", "United States", "Mexico"]
print(list_nation)

# List Methods: 
# .pop() -> Remove and return a single item at index 
local_banks = ["OCBC", "POSB", "DBS", "UOB"]
local_banks.pop() # pop will remove the last item of the list by default
print(local_banks)
# in order to remove a specific item in the list using pop: 
local_banks.pop(1)  #POSB will be removed instead
local_banks.pop(-1) # A negative index will remove the last element -> Eg -1 will remove UOB, -2 will remove DBS, -3 will remove POSB, -4 will remove OCBC

# .insert() -> Insert a single item before an index 
local_banks = ["OCBC", "POSB", "DBS", "UOB"]
local_banks.insert(0,"Citibank") 
print(local_banks) #Citibank will not take the 0 position and come before OCBC

# .append() -> Append a single item to the end of a list
local_banks = ["OCBC", "POSB", "DBS", "UOB"]
local_banks.append("bank of china") # bank of china will now be inserted at the end of the list
print(local_banks)

# .extend() -> Add several items to the end of a list 
local_banks = ["OCBC", "POSB", "DBS", "UOB"]
new_banks = ("citibank", "rabobank", "bank of china")
local_banks.extend(new_banks)
print(local_banks)
# the extend function can take in a tuple () or a list []

# Iterables: 
# Lists. tuples, dictionaries, are also known as iterables 
# An iterable is any python object capable of returning its members one at a time

# List: Append Method 
# .append() attribute is only meant for list objects 
# When .append() is used on a tuple, you will encounter a AttributeError exception 
numbers = [1,2,3,4,5]

empty_list = []

for num in numbers: 
    empty_list.append(num*10)
print(empty_list)

# Built in Functions : 
# sum() -> adds the value of each element of an iterable 
# min() -> finds the lowest value of an iterable 
# max() -> finds the highest value of an iterable
temperature = [10.4, 20.2, 31.5, 22.1, 5.7]
avg = sum(temperature) / len(temperature)
print(f"average tem: {avg} \nminimum temp: {min(temperature)} \nmaximum temp: {max(temperature)}")

# Nested Iterables, Sort and Copy : 
# Nested Iterables: 
list_of_3 = [["savings", "fixed interest"], ["equity", "unit trusts"], ["mortgage", "cpf"]]
print(list_of_3)
print(list_of_3[0]) # To access the first sub list of "savings", "fixed interest"
print(list_of_3[0][0]) # To access the content in the position 0 in the first sub list 

# Sorting Iterables: 
# .sort() for list -> Rearrange the elements in a list 
# .sort() takes 2 parameters: key=None and reversed=False 
# The key parameter accepts a function which can be built in such as len or custom function 
# The reversed parameter will sort the list in descending order 
height_data= [190,165,175,155,182]
car_data=["toyota", "honda", "mazda", "kia", "hyundai"]
height_data.sort()
height_data.sort(reverse=True) # the list will be sorted into descending order instead of in ascending order
car_data.sort()
car_data.sort(key=len) # the strings in the list will be arranged based on the length of the words in the string 
print(height_data)
print(car_data)

#Lists, Conditionals, and Loops: 
sgd= [1200,2400,955,3420,10400,7300,100000,6300,5500,4320]
lower_forex=0.71
higher_forex=0.74

lowerforex_bucket=[]
higherforex_bucket=[]

for amount in sgd: 
    if amount >= 10000: 
        lowerforex_bucket.append(amount*lower_forex)
    else: 
        higherforex_bucket.append(amount*higher_forex)
print(lowerforex_bucket)
print(higherforex_bucket)

# Dictionaries: 
# Structural Data -> Data that are tabular, in rows and columns. For example, spreadsheets
# Unstructural Data -> Data that does not come tabular. For example, images, videos, sound bites 
# Semi-structural Data -> Data has some structures but is not tabular. For example, JSON and XML 
# Unstructural and Semi-structural Data require further processing to convert them to tabular form before they can be used in business context

# Key-value pairs: 
# A dictionary holds information as a pair of data with a key and the value associated with the key
# A dictionary needs a key before storing a value 
# Each key is assigned to a single value 

# Dictionary Literal: 
# Dictionaries : key/value pair 
best_artist= { 
    "pop" : "one direction",
    "opera": "josh groban", 
    "jazz": "stacy kent",
    "classical": "2 cellos",
    }
print(best_artist["pop"]) # to access one direction
# Another method to access values in a dictionary is using .get()
# For Example: 
print(best_artist.get("pop"))

# Dictionaries are mutable objects : 
best_artist= { 
    "pop" : "one direction",
    "opera": "josh groban", 
    "jazz": "stacy kent",
    "classical": "2 cellos",
    }
best_artist["pop"] = "dua lipa"
best_artist["rock"] = "bon jovi" # This is to add another key value pair to the dictionary 
del best_artist["opera"] # use del to remove a key value pair 
print(best_artist)

# Iterating over dictionaries: 
best_artist= { 
    "pop" : "one direction",
    "opera": "josh groban", 
    "jazz": "stacy kent",
    "classical": "2 cellos",
    }
for genre in best_artist: 
    print(f"Song genre: {genre}")
for genre in best_artist: 
    print(f"Best Artist: {best_artist[genre]}")

# .items() method in dictionary: 
best_artist= { 
    "pop" : "one direction",
    "opera": "josh groban", 
    "jazz": "stacy kent",
    "classical": "2 cellos",
    }
print(best_artist.items())

for genre, artist in best_artist.items(): 
    print(f"The best artist in {genre} is {artist}!")

# Nested Dictionaries: 
song_title={
    "2002" : { "Artist" : "Ann-Marie",
               "Length" : 234,
               "Album" : "2002", 
               "Genre" : "pop"}, 
    "Forever in love" : { "Artist" : "kenny g", 
                           "Length" : 275.4, 
                           "Album": "breatheless", 
                           "Genre": "jazz"}, 
    "The Prayer" : { "Artist" : "andre bocelli",
               "Length" : 256.8,
               "Album" : "these are special times", 
               "Genre" : "opera"}, 
    "November Rain" : { "Artist" : "Guns n Roses",
               "Length" : 310,
               "Album" : "Use Your Illusions 1", 
               "Genre" : "rock"} 
}
userinput=input("Enter a Song Title: ")
for song in song_title:
    if userinput.upper() == song.upper():
        print(f'song:{song} | Artist:{song_title[song]["Artist"]} | Length: {song_title[song]["Length"]}secs | Genre: {song_title[song]["Genre"]}')

# Access values of a nested dictionary: 
for song in song_title: 
    print(song_title[song]["Length"])
for song in song_title: 
    if song_title[song]["Genre"] == "rock": 
        print(song) # This is to find which song is in the genre of rock 

# User Input with Dictionary: 

    








