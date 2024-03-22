# import the csv module to read csv files
import csv

# Create file path
filepath = "PyBank/Resources/budget_data.csv"

# set the counter of total_rows to zero
total_rows = 0
#set a place to put the total rows 
date_values = set()

#indicating that the column index for the profit/loss is 1
colmn_index = 1

#setting the net_profit_loss is zero
net_profit_loss = 0

#setting the prevous value as non for the change in profit/loss
previous_value = None

#setting the total change in profit is zero
total_change = 0

#setting the change_count is zero
change_count = 0


# Read the header in the CSV file 
with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader: 
        total_rows += 1 #add 1 to total_rows
        date_value = row[1] #set the date to start with index 1 due to header
        if date_value: 
            date_values.add(date_value) #if there is a date value, add it to the date_values
total_no_months = len(date_values) # set the total number of months from the date value
#print(f"Total number of rows in the Date column: {total_rows}")
print(f"Total Months: {total_no_months}") 

# to find and print the net total amount of "Profit/Losses" over the entire period
with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader: 
                profit_loss = float(row[1])
                net_profit_loss += profit_loss
avg_profit_loss = net_profit_loss/total_no_months
print(f"Total: ${net_profit_loss}")

# to find and print the changes in "Profit/Losses" over the entire period, and then the average of those changes
with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader: 
        profit_loss = int(row[1])
        if previous_value is not None:
             change = profit_loss - previous_value
             total_change += change
             change_count +=1
        previous_value = profit_loss
if change_count > 0:
     average_change = total_change/change_count
print(f"Average Change: ${average_change:0.2f}")


# to find and print the greatest increase in profits (date and amount) over the entire period
with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    max_increase = 0
    max_increase_date = None
    previous_profit = None
    for row in csvreader: 
            date = row[0]
            profit = int(row[1])
            if previous_profit is not None:
                 increase = profit - previous_profit
                 if increase > max_increase:
                      max_increase = increase
                      max_increase_date = date
            previous_profit = profit
    if max_increase_date is not None:
         print(f"The greatest increase in profits: {max_increase_date} (${max_increase})")
# to find and print the greatest decrease in profits (date and amount) over the entire period
    with open(filepath, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        max_decrease = 0
        max_decrease_date = None
        previous_profit = None
        for row in csvreader: 
            date = row[0]
            profit = int(row[1])
            if previous_profit is not None:
                 decrease = profit - previous_profit
                 if decrease < max_decrease:
                      max_decrease = decrease
                      max_decrease_date = date
            previous_profit = profit
    if max_decrease_date is not None:
         print(f"The greatest decrease in profits: {max_decrease_date} (${max_decrease})")

#setting up the file path to save the output file and printing data as text file
fileoutpath = "PyBank/analysis/budget_data_analysis.txt"
with open(fileoutpath, "w") as budget_data_analysis:
     budget_data_analysis.write("Financial Analysis\n")
     budget_data_analysis.write("---------------------\n")
     budget_data_analysis.write(f"Total Months: {total_no_months}\n")
     budget_data_analysis.write(f"Total: ${net_profit_loss}\n")
     budget_data_analysis.write(f"Average Change: ${average_change:0.2f}\n")
     budget_data_analysis.write(f"The greatest increase in profits: {max_increase_date} (${max_increase})\n")
     budget_data_analysis.write(f"The greatest decrease in profits: {max_decrease_date} (${max_decrease})")





         






