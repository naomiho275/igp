from pathlib import Path
import matplotlib.pyplot as plt # ensure you have intalled matplotlib before importing it. available in the project brief.
import csv

#--------------- PART 1: This part of the program is completed for you --------------#

# create a file to csv file.
fp = Path.cwd()/"superstore_transaction.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create 3 empty lists to store profit and quantity by each cluster
    cluster1 = [] 
    cluster2 = []
    cluster3 = []

    # append profit and quantity as a list back to each empty list
    for row in reader:
                
        if row[4] == "Cluster 1":
            cluster1.append([row[13], row[14]])
        elif row[4] == "Cluster 2":
            cluster2.append([row[13], row[14]])
        else:
            cluster3.append([row[13], row[14]])

#---------------------------- PART 2: Insert your own code ---------------------------#
# 1. Calculate the total profit and total quantity using cluster 1,2,3 variables from part 1
# 2. Write the calculated profit to a txt file. Name it as cluster_report.txt.

# This is to import path method from pathlib
from pathlib import Path
# This is to create a file path to the computer's home directory 
file_path = Path.home()/"cluster_report.txt"
# Creating a new .txt file to store the calculated total profit and total quantity 
file_path.touch()    
# Create a function that has 1 parameter to calculate the total profit using the cluster variables 
def profit_calc(cluster):
    """
    - This function calculates the total profit 
    - This function accepts 1 parameter : cluster 
    """
    # This is to create a variable and assign the value of 0 to store the values and so that total+=data is 0 + data
    total_Profit = 0
    # using a for loop to loop the data from clusters 1,2, and 3
    for data in cluster:
        # Checking if there is a negative symbol at the beginning of the value ( index position 0 )
        if data[0][0]=='-':
            # Replacing the dollar sign symbol $ at the beginning of the value with an empty space 
            new_profit = data[0].replace("$", "")
            # Replacing , with an empty space 
            new_profit = new_profit.replace(",", "")
            # Calculating the total profit by adding the new profit to the total profit of 0 
            total_Profit += float(new_profit)
        # Checking if the value is positive and has no negative symbol 
        else:
            # Replacing the dollar sign symbol $ with an empty space 
            new_profit = data[0].replace("$", "")
            # Replacing the , with an empty space 
            new_profit = new_profit.replace(",", "")
            # Adding the value of 0 which is the total to new profit in order to calculate the total profit 
            total_Profit += float(new_profit)
    # return the total calculated profit to the main program 
    return total_Profit 

# Creating a function to calculate the total quantity 
def quantity_calc(cluster):
    """
    - This function calculates the total quantity 
    - This function accepts 1 parameter : cluster 
    """
    #This is to create a variable to store the values and assign the value of 0 so that total+=data is 0 + data
    total_Quantity =0
    #using a for loop to loop the data from the clusters 
    for data in cluster: 
        # Calculating the total quantity by adding the total quantity of 0 to the quantity which is found in index position 1 of each of the clusters 
        total_Quantity += float(data[1])
    # Return the total calculated quantity to the main program 
    return total_Quantity
   
# This is to open a file using "with" and "open" keyword in write mode 
with file_path.open(mode="w", encoding="UTF-8") as file:
    # Writing the respective total profits of Clusters 1,2,3 into the cluster_report.txt file 
    file.write(f"PROFIT REPORT\n=============\nCluster 1: ${profit_calc(cluster1)}\nCluster 2: ${profit_calc(cluster2)}\nCluster 3: ${profit_calc(cluster3)}\n")
    # Writing the respective total quantity of Clusters 1,2,3 into the cluster_report.txt file 
    file.write(f"\nQUANTITY REPORT\n===============\nCluster 1: {quantity_calc(cluster1)}\nCluster 2: {quantity_calc(cluster2)}\nCluster 3: {quantity_calc(cluster3)}")

#--------------- PART 3: This part of the program is completed for you  --------------#

# This part of the program plots the profits and quantities by clusters.
# The values profits and quantities are hard-coded, so it is not link to part 2. 
# Even if part 2 does not work, part 3 can still be executed.
# Simply execute the code and the plot will be saved as an image file.
# Click on the png file in the explorer panel to see the barplot.

# Do not worry about how the code below works.
# It is an example of visualising data using Python. 
# You will learn about data visulisation in analytics module in year 2. 

cluster_profit = [133426, 43684, 109224] # hardcoded profit by clusters 
cluster_quantity = [18632, 8716, 10524] # hardcoded quantity sold by clusters. 
fig, axs = plt.subplots(2, figsize = (10,7))
fig.suptitle("SuperStore Business Performance")
cluster = ["cluster 1", "cluster 2", "cluster 3"]
axs[0].bar(cluster, cluster_profit)
axs[1].bar(cluster, cluster_quantity)
axs[0].set_xlabel("Profit by Clusters")
axs[1].set_xlabel("Quantity Sold by Clusters")
axs[0].set_ylabel("Profit ($)")
axs[1].set_ylabel("Quantity (000s)")
fig.savefig("cluster_barplot.png") 
plt.imread("cluster_barplot.png")
plt.show()












