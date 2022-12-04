import os
import csv

election_data_csv=os.path.join("Resources/election_data.csv")

candidate_votes={}
candidate_list=[]
total_votes=0

winning_candidate=""
winning_count=0
   
print("``` text ")
print("Election Results")
print("-------------------------------------")

with open(election_data_csv) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=",")
    header=next(csv_reader)
    for row in csv_reader:
        total_votes +=1
        candidate=str(row[2])

        if candidate not in candidate_list:
            candidate_list.append(str(candidate))
            candidate_votes[candidate]=0
        candidate_votes[candidate] +=1
        
print(f"Total Votes: {total_votes}")
print("-------------------------------------")
for candidate in candidate_votes:
    votes=candidate_votes.get(candidate)
    vote_percentage= 0
    vote_percentage=round(float(votes)/float(total_votes)*100,3)
        
    final_list = (f"{candidate}: {vote_percentage}% ({votes})")
    print(final_list) 
    if votes > winning_count:
        winning_count = votes
        winning_candidate = candidate
print("-------------------------------------")
print(f'Winner: {winning_candidate}')
print("-------------------------------------")
print("``` text ")           



PyPoll= os.path.join(".", 'PyPoll.txt')
with open('PyPoll.txt' , 'w') as text:
    text.write("``` text\n")
    text.write("Election Results\n")
    text.write("-----------------------------------------------\n")
    text.write(f"Total Votes: {total_votes}\n")
    text.write("-----------------------------------------------\n")
    for candidate in candidate_votes:
        votes=candidate_votes.get(candidate)
        vote_percentage= 0
        vote_percentage=round(float(votes)/float(total_votes)*100,3)    
        text.write(f"{candidate}: {vote_percentage}% ({votes})\n")
        
    text.write("-----------------------------------------------\n")
    text.write(f"Winner: {winning_candidate}\n")
    text.write("-----------------------------------------------\n")
    text.write("``` text")