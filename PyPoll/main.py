# import dependencies and packages
import os
import csv

# Files to load and output:
file_to_load = os.path.join("Resources", "election_data_test.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

## declare/initalize variables
#1. Total # of votes cast
#2. Complete list of candidates who received votes
#3. Percentage of votes each candidate won
#4. Total # of votes each candidate won
#5. Winner of election based on popluar vote
 
#total_votes
#total_votes_per_candidate_percentage
#election_winner
#row_count
#results [store candidates names and # votes per candidate]

#Initializing variables
total_votes = 0
vote_count = 0
total_votes_per_candidate_percentage = 0
election_winner = ""
row_count = 0
results = []

# open csv file
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

# For every row in the file: read the row and accumalate in results list
    for row in reader:
        if row_count != 0:
            print(row[2])
# Returns the index of the first object with a matching value
            if row [2] in results:
                print('candidate in the list')
            else:
                print('candidate not in list')
            total_votes = total_votes + 1
# Add 1 candidate to the candidate_count in results (Add an element onto the end of a List)
# Else add candidate name to results list and set candidate count to 1 in results list
results.append(row [2])
print(results)
# add 1 to vote_count
vote_count = vote_count + 1
       
       
row_count = row_count + 1

##Print end export results

print('Election Result')
print('----------------------------')
print('Total Votes', total_votes)
print('----------------------------')
