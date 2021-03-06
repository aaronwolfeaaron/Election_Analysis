# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}

# County options and county votes.
county_names = []
county_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Track the largest county and county voter turnout.
largest_county_turnout = ""
largest_county_vote = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    header = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count.
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        #Get the county name from each row.
        county_name = row[1]

        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
            # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        # If the county does not match any existing county, add to the county list.
        if county_name not in county_names:
            # Add the county name to the county list.
            county_names.append(county_name)
            # And begin tracking that county's voter count.
            county_votes[county_name] = 0
            # Add a vote to that county's count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file, print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes:\n"
    )
    print(election_results, end="") 
    
    txt_file.write(election_results)

    for county in county_votes:
        # Retrieve vote count and percentage.
        county_vote = county_votes[county]
        county_percent = float(county_vote) / float(total_votes) * 100
        county_results = (
            f"{county}: {county_percent:.1f}% ({county_vote:,})\n")
        print(county_results, end="")
        if (county_vote > largest_county_vote):
            largest_county_vote = county_vote
            largest_county_turnout = county
    txt_file.write(county_results)
 
    # Print the winning county's results to the terminal.
    largest_county_turnout = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"-------------------------\n"
    )

    print(largest_county_turnout)
    
    txt_file.write(largest_county_turnout)       

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = int(votes) / int(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n"
        )
        print(candidate_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

        txt_file.write(candidate_results)

    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    #Save the candidate with the largest voter turnout to a text file.
    txt_file.write(winning_candidate_summary)