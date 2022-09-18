import os
import csv

file_to_load = "resources/budget_data.csv"
file_to_output = "analysis/analysis.txt"

total_months= 86
month_of_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999]
total_profitloss = 0


with open(file_to_load, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        total_months = 86
    

        if (total_profitloss > greatest_increase[1]):
            greatest_increase[0] = row["date"]
            greatest_increase[1] = total_profitloss
            
            if (total_profitloss < greatest_decrease[1]):
                greatest_decrease[0] = row["date"]
                greatest_decrease[1] = total_profitloss

output =(
    f"\nFinancial Anaylsis\n"
    f"----------------------\n"
    f"total Months:(total_months)\n"
    f"total:(total_profitloss)\n"
    f"greatest Increase in profitsloss: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"greatest Decrease in profitsloss: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

print(output)



with open(file_to_output, 'w') as csvfile:
    writer = csv.writer(csvfile)
    



