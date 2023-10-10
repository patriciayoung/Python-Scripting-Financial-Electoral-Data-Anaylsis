# Python-challenge
Before running any code need to find your way to the current working directory in the terminal ( I was doing this in the terminal in VS code to get to the correct directory to be able to run the code; for both PyBank and PyPoll)


PyBank pseudo-code
1. Total # of months
2. Net P&L
3. Average change on P&L
4. Greatest increase (date & amount)
5. Greatest decrease (date & amount)
 
 
total_months
total_pandl
average_change
greatest_increase_date
greatest_increase_pandl
greatest_decrease_date
greatest_decrease_pandl
previous_pandl
row_count
change_pandl
 
#Initializing variables
total_months = 0
total_pandl = 0
change_pandl =0
average_change = 0
row_count = 0
greatest_increase_pandl = 0
greatest_decrease_pandl = 0
 
 
FOR every row in the file
        IF row_count=0
        THEN
do nothing
        ELSE
                        IF row_count = 1
                        THEN
                                        Previous_pandl = file_pandl
                                total_months = total_months+1
total_pandl = total_pandl + file_pandl
                        ELSE
                                total_months = total_months+1
                                total_pandl = total_pandl + file_pandl
                                change_pandl = file_pandl – previous_pandl
                                average_change=average_change+change_pandl
                                IF change_pandl > greatest_increase_pandl
                                THEN
                                                greatest_increase_pandl = change_pandl
                                                greatest_increase_date=file_date
                                ENDIF
                                IF change_pandl < greatest_decrease_pandl
                                THEN
                                                Greatest_decrease_pandl = change_pandl
                                                Greatest_decrease_pandl = file_date
                                ENDIF
                                        Previous_pandl = file_pandl
                ENDIF
        ENDIF
row_count=row_count + 1
Read the next row
END FOR
Average_change= average_change/(total_months-1)
 
#Print end export results
 
Print(“Financial Analysis”)
Print(“--------------------------------------------------“)
Print(“Total Months: “,total_months)
Print(“Total: “,total_pandl)
Print(“Average change: “,average_change)
Print(“Greatest increase in profits”,greatest_increase_date, greatest_increase_pandl)
Print(“Greatest decrease in profits”,greatest_decrease_date, greatest_decrease_pandl)
 
Export to text file




PyPoll Pseudo-code:

# import dependencies and packages
# Files to load and output:

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

# open csv file

# For every row in the file: read the row and accumalate in results list

# Add 1 candidate to the candidate_count in results (Add an element onto the end of a List)
# Else add candidate name to results list and set candidate count to 1 in results list

# Returns the index of the first object with a matching value

# add 1 to vote_count

##Print end export results

# Tallying results list /  Percentage

# exporting to text file

