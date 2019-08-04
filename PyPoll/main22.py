import os
import csv

budget_file = os.path.join("Resources", "election_data.csv")

with open(budget_file, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_head = next(csv_reader)

    total_vote = 0
    candidates_list = []
    total_C_votes = []
    Cpercent = []

    for row in csv_reader:
        total_vote += 1

        if row [2] in candidates_list:
            name = row[2]
            index_looking_for = candidates_list.index(name)
            total_C_votes[index_looking_for]+=1

        else:
            candidates_list.append(row[2])
            total_C_votes.append(1)
            
f = open("output.txt","w")
print(candidates_list)
f.write
print("Election Results")
f.write("Election Results \n")
print("-----------------")
f.write("----------------- \n")
print ("Total Votes " + (str(total_vote)))
f.write("Total Votes " + (str(total_vote))+"\n")
print("----------------------")
f.write("----------------------\n")

for row in range(len(total_C_votes)):
    row/total_vote
    Cpercent = row/total_vote
    print(f'{candidates_list[row]} {round(100*total_C_votes[row]/total_vote,2)}% ({total_C_votes[row]})')
    f.write(f'{candidates_list[row]} \n {round(100*total_C_votes[row]/total_vote,2)}% \n ({total_C_votes[row]})')

print("---------------------\n")
print ("Winner Khan")




  
    
