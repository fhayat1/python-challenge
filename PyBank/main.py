import os
import csv

file_to_load = "Resources/budget_data.csv"
file_to_output = "analysis/analysis.txt"

total_months= 0  
month_of_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]
current_profitloss = 0
running_total = 0
prev_profitloss = 0

with open(file_to_load, 'r') as csvfile:
    reader = csv.reader(csvfile)
    headers=next(reader,None)
    for row in reader:
        
        total_months = total_months +1
        current_profitloss = int(row[1]) 
        running_total = running_total + current_profitloss

        if prev_profitloss < 0: 
            if ((current_profitloss + abs(prev_profitloss)) > greatest_increase[1]):
                greatest_increase[0] = row[0]
                greatest_increase[1] = current_profitloss + abs(prev_profitloss)
            
        if prev_profitloss > 0 and current_profitloss < 0: 
            if ((current_profitloss +(-1* prev_profitloss)) < greatest_decrease[1]):
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = current_profitloss +(-1* prev_profitloss)  
        prev_profitloss = int(row[1])
output =(
    f"\nFinancial Anaylsis\n"
    f"----------------------\n"
    f"total Months: {total_months}\n"
    f"total: {running_total}\n"
    f"average change: {running_total/total_months}\n"
    f"greatest Increase in profitsloss: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"greatest Decrease in profitsloss: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

print(output)



with open(file_to_output, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output)




