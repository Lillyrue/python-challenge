#modules
import os

import csv

#create csv path
csvpath = os.path.join('Resources', 'budget_data.csv')

csvpath_output = os.path.join ('Analysis', 'Financial_Analysis.txt')

#set variables for analysis
Total_months = 0
total = 0
change = 0
total_change = 0
previous_profit = 0
count = 0



#open the csv file
with open(csvpath) as csvfile:
   csv_reader = csv.reader(csvfile, delimiter=',')
    
   csv_header = next(csv_reader)
   
   
   for row in csv_reader:
        Total_months = Total_months + 1
        total = total + int(row[1])
        
        current_profit = int(row[1])
        
        if previous_profit != 0:
            change = current_profit - previous_profit 
            total_change = total_change + change
            count = count + 1
            
        previous_profit = current_profit
        
        
        
        
#count the number of months
print(Total_months)

    
#Sum the net total amount of "Profit/Losses" over entire time period
print(total)   
    
#Find the changes in "Profit/Losses" during time period and calculate the average of those changes
print(total_change/count)
print(count)

    
#Find the greatest increase in profits that includes date and amount
  

#Find the greatest decrease in profits that includes dates and amount


    
output = f"""
Financial Analysis
----------------------------
Total Months: {Total_months}
Total: ${total}
Average Change: ${total_change/count:.2f}
Greatest Increase in Profits: 
Greatest Decrease in Profits:
"""

print(output)

with open(csvpath_output, "w") as textfile:
    textfile.write(output)

