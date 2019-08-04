import os
import csv

budget_file = os.path.join("Resources", "budget_data.csv")

total_months = 0
changed_months = []
netchange_list = []
increased_value = ["", 0]
decreased_value = ["", 9999999999999999999]
total_net = 0

with open(budget_file) as financial_data:
    reader = csv.reader(financial_data)

    header = next(reader)

    first_row = next(reader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        total_months = total_months + 1
        total_net = total_net + int(row[1])

        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        netchange_list = netchange_list + [net_change]
        changed_months = changed_months + [row[0]]

        if net_change > increased_value[1]:
            increased_value[0] = row[0]
            increased_value[1] = net_change

        if net_change < decreased_value[1]:
            decreased_value[0] = row[0]
            decreased_value[1] = net_change

avg_net_month = sum(netchange_list) / len(netchange_list)

f = open("budget_output.txt","w")
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${avg_net_month:.2f}\n"
    f"Greatest Increase in Profits: {increased_value[0]} (${increased_value[1]})\n"
    f"Greatest Decrease in Profits: {decreased_value[0]} (${decreased_value[1]})\n")

f = open("budget_output.txt","w")
print(output)
f.write(output)


