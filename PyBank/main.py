import os
import csv

#path to collect data from the resources folder

budget_data_csv = os.path.join("Resources/budget_data.csv")


#Create empty list
month_count=[]
profit_losses=[]
change=[]

with open(budget_data_csv) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)
    
    for row in csv_reader:
        month_count.append(str(row[0]))
        profit_losses.append(int(row[1]))
    
   
    for i in range(len(profit_losses)-1):
       
        change.append(profit_losses[i+1]- profit_losses[i])
    
    Increase=max(change)
    Decrease=min(change)
    month_increase=change.index(max(change))+1
    month_decrease=change.index(min(change))+1    
    
print("Financial Analysis")
print("-----------------------------------------------")
print(f'Total Months: {str(len(month_count))}')
print(f'Total: ${sum(profit_losses)}')
print(f"Average Change: {round(sum(change)/ len(change),2)}")
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(Increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(Decrease))})")

pyBank= os.path.join(".", 'pyBank.txt')
with open('pyBank.txt' , 'w') as text:
    text.write("Financial Analysis\n")
    text.write("-----------------------------------------------\n")
    text.write(f'Total Months: {str(len(month_count))}')
    text.write("\n")
    text.write(f'Total: ${sum(profit_losses)}')
    text.write("\n")
    text.write(f"Average Change: {round(sum(change)/ len(change),2)}")
    text.write("\n")
    text.write(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(Increase))})")
    text.write("\n")
    text.write(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(Decrease))})")
               