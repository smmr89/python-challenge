#%%
import os
import csv
# set paths
budget_csv = os.path.join("Resources", "budget_data.csv")           # path for retrieving csv data
analysis_txt = os.path.join("analysis", "results.txt")              # path for creating txt file
# assign lists
dates = []                                                          # dates list
profit = []                                                         # profit list
profit_changes = []                                                 # profit change list
# initialise variables to zero
profit_prior = 0
months = 0
total_profit = 0
average_change = 0

max_profit_change = 0
min_profit_change = 0

with open(budget_csv) as csvfile:                                   # open csv file
    csv_reader = csv.reader(csvfile, delimiter=",")         
    # csv_header = next(csvfile)                                      # read the header and skips it
    next(csvfile)
    for row in csv_reader:
        date = row[0]                                               # read date each row
        profit = int(row[1])                                        # read profit in each row and convert to integer


        months += 1                                                 # tally months (each row)
        
        total_profit += profit                                      # sum the profit/loss

        if months > 1:                                              # need at least 2 months to calculate change

            profit_changes.append(profit - profit_prior)            # populate profit_changes list
            
            dates.append(date)                                      # populate dates list
        
        profit_prior = profit                                       # set prior profit to "current" month

average_change = sum(profit_changes) / len(profit_changes)          # calculate average_chnage

max_profit_change = max(profit_changes)                             # max profit
min_profit_change = min(profit_changes)                             # min profit

results = f'''#######################################################
################   Financial Analysis  ################
#######################################################
      
-------------------------------------------------------
      
Total Months:                       {months}

Total:                              ${total_profit}

Average Change:                     ${average_change:.2f}

Greatest Increase in Profits:       {dates[profit_changes.index(max_profit_change)]} (${max_profit_change})

Greatest Decrease in Profits:       {dates[profit_changes.index(min_profit_change)]} (${min_profit_change})'''

print(results)                                                      # print to screen

with open(analysis_txt,'w') as txtfile:                             # open new file
    txtfile.write(results)                                          # write to file