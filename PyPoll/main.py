# import dependencies and packages
# import os
import csv

# open csv file
with open("Bootcamp", "Homework/Challenges", "Python-challenge", 
          "Starter_Code", "PyPoll", "Resources", "election_data.csv") as csv_file:

# read csv file row by row AND # skip header row
    csvreader = csv.reader(csv_file)
    next(csvreader)

# create list to store candidate votes
candidate_votes = []

# repeat over rows 
for row in csvreader:

    # candidate name
    candidate_name = row[2]

    # print candidate name
    print(csv_file.read())
