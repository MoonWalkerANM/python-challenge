# import the csv module to read csv files
import csv

# Create file path
filepath = "PyPoll/Resources/election_data.csv"

#set variables to store the data required
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

#read csv file
with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader) #set the header row and skip it
    for row in csvreader:
        total_votes += 1 # adding 1 to total_vote if row has value
        name_of_candidate = row[2]
        if name_of_candidate in candidates:
            candidates[name_of_candidate] +=1
        else:
            candidates[name_of_candidate] = 1

#calculating the percentage for each winning candidate
for candidate, votes in candidates.items():
    percentage = (votes/total_votes) * 100
    candidates[candidate] = {"votes": votes, "percentage": percentage}

#check for the winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

#print the results
     
print(f"Total Votes: {total_votes}")
for candidate, data in candidates.items():
    print(f"{candidate}: {data['percentage']:.3f}% ({data['votes']})")
print(f"Winner: {winner}")

#setting up the file path to save the output file and printing data as text file
fileoutpath = "PyPoll/analysis/election_data_analysis.txt"
with open(fileoutpath, "w") as election_data_analysis:
     election_data_analysis.write("Election Results\n")
     election_data_analysis.write("---------------------\n")
     election_data_analysis.write(f"Total Votes: {total_votes}\n")
     election_data_analysis.write("---------------------\n")
     for candidate, data in candidates.items():
        election_data_analysis.write(f"{candidate}: {data['percentage']:.3f}% ({data['votes']})\n")   
     election_data_analysis.write("---------------------\n")
     election_data_analysis.write(f"Winner: {winner}\n")
     election_data_analysis.write("---------------------\n")
    