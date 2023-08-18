#%%
import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")       # Set path for csv
analysis_txt = os.path.join("analysis", "results.txt")              # Set path for export txt

Votes_Analysis = {"Candidate":[],"Votes":[]}                        # Dictionary to collect data
#initialise values
votes = 0
rowcount = 0
prior_candidate = "hello there"
first_candidate = "dude"
initial_row_index = 1

with open(election_csv) as csvfile:                                 # open csv file
    csv_reader = csv.reader(csvfile, delimiter=",")         
    csv_header = next(csvfile)                                      # read the header and store it

    for row in csv_reader:
        rowcount += 1                                               # get no of rows
        if rowcount == 1:                                           # initialise first row of data
            first_candidate = row[2]
            Votes_Analysis["Candidate"].append(row[2])
            prior_candidate = first_candidate

    
with open(election_csv) as csvfile:                                 # open csv file
    csv_reader = csv.reader(csvfile, delimiter=",")                 
    csv_header = next(csvfile)                                      # read the header and store it

    for row in csv_reader:
        votes += 1                                                  # count votes


        if row[2] != prior_candidate:                               # tally votes for change in candidate
            Votes_Analysis["Candidate"].append(row[2])
            vote_count = votes - initial_row_index
            Votes_Analysis["Votes"].append(vote_count)
            initial_row_index = votes

        if votes == rowcount:                                       # count up the last section till end
            vote_count = votes - initial_row_index + 1
            Votes_Analysis["Votes"].append(vote_count)

        prior_candidate = row[2]

# initialise variables to count
count1 = 0
count2 = 0
count3 = 0

# count variables
for i in range(len(Votes_Analysis["Candidate"])):
    if Votes_Analysis["Candidate"][i] == "Charles Casper Stockham":
        count1 += Votes_Analysis["Votes"][i]

    if Votes_Analysis["Candidate"][i] == "Diana DeGette":
        count2 += Votes_Analysis["Votes"][i]

    if Votes_Analysis["Candidate"][i] == "Raymon Anthony Doane":
        count3 += Votes_Analysis["Votes"][i]

# assemble data into Final_Count dictionary
Final_Count = {"Charles Casper Stockham":count1,
               "Diana DeGette":count2,
               "Raymon Anthony Doane":count3}


# print and export results
results = f'''#######################################################
#################   Election Results  #################
#######################################################
      
-------------------------------------------------------

Total Votes:                        {votes}

-------------------------------------------------------

Charles Casper Stockham:            {(count1/votes)*100:.3f}% ({count1})

Diana DeGette:                      {(count2/votes)*100:.3f}% ({count2})

Raymon Anthony Doane:               {(count3/votes)*100:.3f}% ({count3})

-------------------------------------------------------

Winner:                             {max(Final_Count, key=Final_Count.get)}

-------------------------------------------------------
'''

print(results)

with open(analysis_txt,'w') as txtfile:                             # open new file
    txtfile.write(results)                                   