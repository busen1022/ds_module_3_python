# Module
import csv

# Set path for csv resource file
csvpath = "Resources/budget_data.csv"
output_path = "analysis/analysis.txt"

# Variables
month_counter = 0
total_profit_loss = 0

prior_month = 0
profit_change_monthly = []
change_monthly = []

# Open the csv with UTF-8 encoding
with open(csvpath, encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read Header Row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:

        # Counter for months
        month_counter += 1

        # Sum of total profit/loss
        total_profit_loss = total_profit_loss + int(row[1])

        # Track monthly change in profit
        if (month_counter == 1):
            prior_month = int(row[1])
        else:
            difference =  int(row[1]) - prior_month
            profit_change_monthly.append(difference)
            prior_month = int(row[1])
            change_monthly.append(row[0])

    # Metrics
    avg_profit_change = sum(profit_change_monthly) / len(profit_change_monthly)
    avg_profit_change = round(avg_profit_change, 2)

    greatest_change = max(profit_change_monthly)
    greatest_month_index = profit_change_monthly.index(greatest_change)
    greatest_month = change_monthly[greatest_month_index]

    worst_change = min(profit_change_monthly)
    worst_month_index = profit_change_monthly.index(worst_change)
    worst_month = change_monthly[worst_month_index]


    print("Financial Analysis")
    print("------------------------------")
    print("Total Months: " + str(month_counter))
    print("Total $" + str(total_profit_loss))
    print("Average Change: $" + str(avg_profit_change))
    print("Greatest Increase in Profits: " + str(greatest_month) + " ($" + str(greatest_change) + ")")
    print("Greatest Decrease in Profits: " + str(worst_month) + " ($" + str(worst_change) + ")")

    # Export to text file (w/ Xpert help)
    with open(output_path, "w") as file:

        file.write("Financial Analysis\n")
        file.write("------------------------------\n")
        file.write("Total Months: " + str(month_counter) + "\n")
        file.write("Total $" + str(total_profit_loss) + "\n")
        file.write("Average Change: $" + str(avg_profit_change) + "\n")
        file.write("Greatest Increase in Profits: " + str(greatest_month) + " ($" + str(greatest_change) + ")\n")
        file.write("Greatest Decrease in Profits: " + str(worst_month) + " ($" + str(worst_change) + ")\n")

    print("File saved to ", output_path)