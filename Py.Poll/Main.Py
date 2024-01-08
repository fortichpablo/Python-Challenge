import csv

# Read data CSV file
with open("/Users/pablofortich/Desktop/Python Challenge/PyPoll/Resources/election_data.csv", "r") as file:
    lines = file.readlines()

# headers and data
headers = lines[0].strip().split(",")
data = [line.strip().split(",") for line in lines[1:]]

# total votes
total_votes = len(data)

# Sort candidates
candidates = set(row[2] for row in data)

# variables to store candidate votes
candidate_votes = {candidate: 0 for candidate in candidates}

# Loop through the data to count votes for every candidate
for row in data:
    candidate_votes[row[2]] += 1

# Calculation of percentage
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Code to find winner
winner = max(candidate_votes, key=candidate_votes.get)

# Election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Save into a txt file (election_results.txt)
output_file = "election_results.txt"
with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate in candidates:
        file.write(f"{candidate}: {percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
