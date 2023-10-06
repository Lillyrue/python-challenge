#modules
import os


import csv


#create csv path
csvpath = os.path.join('Resources', 'election_data.csv')


    
csvpath_output = os.path.join('Analysis', 'election_results.txt')



#set variables for analysis
total_votes = 0



#open the csv file
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    print(csv_reader)
    
    
    csv_header = next(csv_reader)
    print(f"csv header: {csv_header}")
    

    
    for row in csv_reader:
        ballot_id = row[0]
        total_votes = total_votes + 1
        
        candidates = row[2]
        
        
        
   
         
        
        
#count the number of total votes
print(total_votes)       

#list the candidates who received votes



#list the percentage of votes for each candidate


#list the number of votes for each candidate


#list the winner of the election based on the popular vote
        
        
output = f"""
Election Results
-------------------------
    Total Votes: {total_votes}
-------------------------

-------------------------

-------------------------
"""

print(output)

with open(csvpath_output, "w") as textfile:
    textfile.write(output)


    