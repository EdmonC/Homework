import csv
import sys
sys.path.append

# Read the dataset and initialize variables
data = []
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# Read the dataset file
with open('PyPoll/Resources/election_data.csv', 'r') as file:
    csvreader = csv.reader(file)
    
    # Skip the header row
    header = next(csvreader)
    
    # Loop through the rows in the dataset
    for row in csvreader:
        # Extract the candidate name from each row
        candidate = row[2]
        
        # Count the total number of votes
        total_votes += 1
        
        # Count the votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Prepare the results as a string
results = "Election Results\n"
results += "-------------------------\n"
results += f"Total Votes: {total_votes}\n"
results += "-------------------------\n"
for candidate, votes in candidates.items():
    # Calculate the percentage of votes each candidate won
    percentage = (votes / total_votes) * 100

    # Append the candidate, percentage, and total votes to the results string
    results += f"{candidate}: {percentage:.3f}% ({votes})\n"

    # Check for the winner based on the popular vote
    if votes > max_votes:
        max_votes = votes
        winner = candidate
results += "-------------------------\n"
results += f"Winner: {winner}\n"
results += "-------------------------\n"

# Write the results to a text file
with open("election_results.txt", "w") as output_file:
    output_file.write(results)

# Print the results to the console
print(results)