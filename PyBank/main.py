# import dependencies and packages
import os
import csv

# Files to load and output:
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("Analysis", "budget_analysis.txt")

# declare variables
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999]
total_net = 0

# read csv file:
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    csvreader = csv.reader(csv_file)
    next(csvreader)

# total number of months included in the dataset
 
# create list for total number months
months = []
 
# repeat over rows
for row in csvreader:

    # total months
    total_months = row[2]

    # print total months
    print(csv_file.read())