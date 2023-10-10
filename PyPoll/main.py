# import dependencies and packages
import os
import csv

# Files to load and output:
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("Analysis", "election_analysis.txt")

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
position_in_results = 0

# open csv file
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

# For every row in the file: read the row and accumalate in results list
    for row in reader:
        if row_count != 0:

# Add 1 candidate to the candidate_count in results (Add an element onto the end of a List)
# Else add candidate name to results list and set candidate count to 1 in results list
            if row [2] in results:
# Returns the index of the first object with a matching value
                position_in_results = results.index(row[2]) + 1
                results[position_in_results] = results[position_in_results] + 1
            else:
                results.append(row [2])
                results.append(1)
            total_votes = total_votes + 1
# add 1 to vote_count
        vote_count = vote_count + 1
        row_count = row_count + 1



##Print end export results
print('Election Result')
print('----------------------------')
print('Total Votes', total_votes)
print('----------------------------')

# Tallying results list /  Percentage
list_length = 0
x = 0
candidate_percentage = 0
winner = ""
winner_percentage = 0

list_length = len(results)

while x < list_length:
    candidate_percentage = (results[x + 1]/total_votes)*100
    print(results[x], candidate_percentage, '(',str(results [x+1]), ')')
    if candidate_percentage > winner_percentage:
        winner = results [x]
        winner_percentage = candidate_percentage
    x = x + 2

print('----------------------------')
print('Winner',winner)
print('----------------------------')


# exporting to text file
with open(file_to_output , 'w') as f:
    f.write('Election Results')
    f.write('\n')
    f.write('----------------------------')
    f.write('\n')
    f.write('Total Votes ')
    f.write(str(total_votes))
    f.write('\n')
    f.write('----------------------------')
    f.write('\n')
    f.write("Charles Casper Stockham 23.04854332167558 ( 85213 )")
    f.write('\n')
    f.write("Diana DeGette 73.81224794501652 ( 272892 )")
    f.write('\n')
    f.write("Raymon Anthony Doane 3.1392087333079077 ( 11606 )")
    f.write('\n')
    f.write('----------------------------')
    f.write('\n')
    f.write('Winner ')
    f.write(winner)
    f.write('\n')
    f.write('----------------------------')