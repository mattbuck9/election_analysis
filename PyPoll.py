# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to load a file from a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []
candidate_votes ={}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1

        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes) * 100

        #To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count/
        if (votes>winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_perfecnt =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
        # To do: print out the winning candidate, vote count and percentage to
        # terminal
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    winning_candidate_summary = (
        f"-----------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------\n")
    print(winning_candidate_summary)

        


   


