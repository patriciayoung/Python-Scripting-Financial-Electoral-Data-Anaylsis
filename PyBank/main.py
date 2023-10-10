# import dependencies and packages
import os
import csv

# Files to load and output:
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("Analysis", "budget_analysis.txt")

## declare/initalize variables
#1. Total # of months
#2. Net P&L
#3. Average change on P&L
#4. Greatest increase (date & amount)
#5. Greatest decrease (date & amount)
 
 
#total_months
#total_pandl
#average_change
#greatest_increase_date
#greatest_increase_pandl
#greatest_decrease_date
#greatest_decrease_pandl
#previous_pandl
#row_count
#change_pandl
 
#Initializing variables
total_months = 0
total_pandl = 0
change_pandl = 0
average_change = 0
row_count = 0
greatest_increase_pandl = 0
greatest_decrease_pandl = 0
greatest_increase_date = ""
greatest_decrease_date = ""

with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    for row in reader:
        if row_count != 0:
            if row_count == 1:
                previous_pandl = int(row [1])
                total_months = total_months + 1
                total_pandl = total_pandl + int(row [1])
            else:
                total_months = total_months+1
                total_pandl = total_pandl + int(row [1])
                change_pandl = int(row [1]) - previous_pandl
                print('change_pandl', change_pandl, row [1], previous_pandl)
                average_change=average_change+change_pandl
                print(change_pandl, greatest_increase_pandl, greatest_decrease_pandl)
                if change_pandl > greatest_increase_pandl:
                    greatest_increase_pandl = change_pandl
                    greatest_increase_date = row [0]
                if change_pandl < greatest_decrease_pandl:
                    greatest_decrease_pandl = change_pandl
                    greatest_decrease_date = row [0]
            previous_pandl = int(row [1])
        row_count=row_count+1

average_change = average_change/total_months




#FOR every row in the file
#        IF row_count=0
#        THEN
#"do nothing"
#        ELSE
#                        IF row_count = 1
#                        THEN
#                                       Previous_pandl = file_pandl
#                                total_months = total_months+1
#total_pandl = total_pandl + file_pandl
#                        ELSE
#                                total_months = total_months+1
#                                total_pandl = total_pandl + file_pandl
#                                change_pandl = file_pandl – previous_pandl
#                                average_change=average_change+change_pandl
#                                IF change_pandl > greatest_increase_pandl
#                                THEN
#                                               greatest_increase_pandl = change_pandl
#                                                greatest_increase_date=file_date
#                                ENDIF
#                                IF change_pandl < greatest_decrease_pandl
#                                THEN
#                                                Greatest_decrease_pandl = change_pandl
#                                                Greatest_decrease_pandl = file_date
#                                ENDIF
#                                        Previous_pandl = file_pandl
#                ENDIF
#        ENDIF
#row_count=row_count + 1
#Read the next row
#END FOR
#Average_change= average_change/(total_months-1)
# 
#Print end export results
# 
print("Financial Analysis")
print(' -------------------------------------------------- ')
print('Total Months: ',total_months)
print('Total: ',total_pandl)
print('Average change: ',average_change)
print('Greatest increase in profits',greatest_increase_date, greatest_increase_pandl)
print('Greatest decrease in profits',greatest_decrease_date, greatest_decrease_pandl)
 
#Export to text file