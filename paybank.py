import csv

# Read the dataset and initialize variables
data = []
total_months = 0
net_profit_loss = 0
previous_profit_loss = 0
profit_loss_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the dataset file
with open('PyBank/Resources/budget_data.csv', 'r') as file:
    csvreader = csv.reader(file)
    
    # Skip the header row
    header = next(csvreader)
    
    # Loop through the rows in the dataset
    for row in csvreader:
        # Extract the date and profit/loss values
        date = row[0]
        profit_loss = int(row[1])
        
        # Calculate the total number of months
        total_months += 1
        
        # Calculate the net total amount of profit/losses
        net_profit_loss += profit_loss
        
        # Calculate the change in profit/loss compared to the previous month
        if previous_profit_loss != 0:
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)
            
            # Check for the greatest increase in profits
            if change > greatest_increase[1]:
                greatest_increase = [date, change]
            
            # Check for the greatest decrease in profits
            if change < greatest_decrease[1]:
                greatest_decrease = [date, change]
        
        # Update the previous profit/loss value for the next iteration
        previous_profit_loss = profit_loss

# Calculate the average change in profit/loss over the entire period
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Prepare the results as a string
results = f"Financial Analysis\n"
results += f"---------------------------------------\n"
results += f"Total Months: {total_months}\n"
results += f"Total: ${net_profit_loss}\n"
results += f"Average Change: ${average_change:.2f}\n"
results += f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
results += f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"

# Open the file in write mode
with open("pybankresult.txt", "w") as output_file:
    output_file.write(results)

# Print the results to the console
print(results)