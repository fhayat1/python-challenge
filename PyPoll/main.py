import os
import csv

#Define the path
csvpath = os.path.join("Resources/election_data.csv")

#set an empty list and dictionaries
total_number_votes = []
candidate = {}
percent_votes = {}

#Open the csv file
with open(csvpath) as csvfile:

    #Read the csv file
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    #loop through the rows in the csv file
    for row in csv_reader:
        
        #Append the rows in the empty list 'total_number votes' and calculate total numbver of votes
        total_number_votes.append(row)
        total_votes = len(total_number_votes)

        #set the key in the dictionary
        key_name = row[2]
        
        #Check whether the key is not in the dictionary 'candidate', if it is then...
        if key_name not in candidate:
            #set the value of the key to 0
            candidate[key_name]= 0
        
        #increase the value of the key each time it encounter the key
        candidate[key_name] += 1

        #calculate the percentage of votes
        percent_calc = (candidate[key_name] / total_votes) * 100
        
        #assign the percent of votes of each candidates to their key
        percent_votes[key_name] = percent_calc
    
        #calculate the maximum of all votes
        max_value = max(percent_votes.values())
        
    #calculate the name of the candidate who got maximum percentage of vote 
    for name, percentage in percent_votes.items():
        if percentage == max_value:
            winner_name = name

#write the output to a new .txt file
pyPoll = open(os.path.join("Analysis/PyPoll.txt"), 'w')

#Print the output in terminal
print("Election Results\n")
print("------------------------------\n")
print("Total Votes: " + str(total_votes) + "\n")
print("------------------------------\n")

#write the output in .txt file
pyPoll.write("Election Results\n")
pyPoll.write("------------------------------\n")
pyPoll.write("Total Votes: " + str(total_votes) + "\n")
pyPoll.write("------------------------------\n")

#sort the dictionary 'percent_votes' and iterate
for new_name, percentage_of_votes in sorted(percent_votes.items(), key=lambda item:item[1], reverse =True):
    print(str(new_name) + ": " + format(percentage_of_votes, '.3f') + "% (" + str(candidate[new_name]) + ")" + "\n")
    pyPoll.write(str(new_name) + ": " + format(percentage_of_votes, '.3f') + "% (" + str(candidate[new_name]) + ")" + "\n")

#Print the output in terminal
print("------------------------------\n")
print("Winner: " + winner_name + "\n")
print("------------------------------")

#write the output in .txt file
pyPoll.write("------------------------------\n")
pyPoll.write("Winner: " + winner_name + "\n") 
pyPoll.write("------------------------------")
pyPoll.close()
