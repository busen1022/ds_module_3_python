# Module
import csv
from collections import Counter  # from Xpert for winner count

# Set path for csv resource file
csvpath = "Resources/election_data.csv"
output_path = "analysis/analysis.txt"

# Opening Variables
total_vote_counter = 0
candidates = []


# Open the csv with UTF-8 encoding
with open(csvpath, encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read Header Row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:

        # Counter for votes
        total_vote_counter += 1

        # Candidate List
        candidates.append(row[2])

    # Remove Duplicate Candidates
    candidate_list = list(set(candidates))

    # Count of each name in "candidates" list
    count_charles = candidates.count("Charles Casper Stockham")
    count_raymon = candidates.count("Raymon Anthony Doane")
    count_diana = candidates.count("Diana DeGette")
        
    # Percentage of total vote for each Candidate
    percent_charles = (int(count_charles) / total_vote_counter) * 100
    percent_charles = round(percent_charles, 3)
    percent_raymon = (int(count_raymon) / total_vote_counter) * 100
    percent_raymon = round(percent_raymon, 3)
    percent_diana = (int(count_diana) / total_vote_counter) * 100
    percent_diana = round(percent_diana, 3)

    # From Xpert for most common counter
    candidate_counter = Counter(candidates)
    winner_candidate = candidate_counter.most_common(1)[0]
    


    print("Election Results")
    print("------------------------------")
    print("Total Votes: " + str(total_vote_counter))
    print("------------------------------")
    print("Charles Casper Stockham: " + str(percent_charles) +"% " + "(" + str(count_charles) + ")")
    print("Diana DeGette: " + str(percent_diana) +"% " + "(" + str(count_diana) + ")")
    print("Raymon Anthony Doane " + str(percent_raymon) +"% " + "(" + str(count_raymon) + ")")
    print("------------------------------")
    print("Winner: " + str(winner_candidate[0]))
    print("------------------------------")


    # Export to text file (w/ Xpert help)
    with open(output_path, "w") as file:

        file.write("Election Results\n")
        file.write("------------------------------\n")
        file.write("Total Votes: " + str(total_vote_counter) + "\n")
        file.write("------------------------------\n")
        file.write("Charles Casper Stockham: " + str(percent_charles) +"% " + "(" + str(count_charles) + ")\n")
        file.write("Diana DeGette: " + str(percent_diana) +"% " + "(" + str(count_diana) + ")\n")
        file.write("Raymon Anthony Doane " + str(percent_raymon) +"% " + "(" + str(count_raymon) + ")\n")
        file.write("------------------------------\n")
        file.write("Winner: " + str(winner_candidate[0]) + "\n")
        file.write("------------------------------\n")

    print("File saved to ", output_path)