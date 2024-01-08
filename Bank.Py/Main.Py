import csv

# file path
file_path = "/Users/pablofortich/Desktop/Python Challenge/PyBank/Resources/budget_data.csv"

# variables
total_months = 0
net_total = 0
previous_profit_loss = 0
monthly_changes = []
months = []

# Read CSV file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip header row
    header = next(csvreader)
    
    # Loop through every single row 
    for row in csvreader:
        # Pull date and profit/loss values
        date = row[0]
        profit_loss = int(row[1])
        
        # Calculation for the number of months
        total_months += 1
        
        # Calculation of the net total of profit/losses
        net_total += profit_loss
        
        # Calculation for change in profit/loss
        if total_months > 1:
            monthly_change = profit_loss - previous_profit_loss
            monthly_changes.append(monthly_change)
            months.append(date)
        
        # Update the previous profit/loss for the next loop
        previous_profit_loss = profit_loss

# Calculation for average change
average_change = sum(monthly_changes) / len(monthly_changes)

# Greatest increase and decrease in profits
greatest_increase = max(monthly_changes)
greatest_decrease = min(monthly_changes)

# Months greatest increase and decrease
greatest_increase_month = months[monthly_changes.index(greatest_increase)]
greatest_decrease_month = months[monthly_changes.index(greatest_decrease)]

# Financial analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Transfer to txt file 
output_file_path = "financial_analysis.txt"
with open(output_file_path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

print(f"Financial analysis results have been saved to {output_file_path}.")


