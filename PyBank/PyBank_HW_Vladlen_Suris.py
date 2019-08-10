# I worked on this code in Jupyter and exported to VSCode hence all the "prints" for testing code
## Decided to not iterate/loop for PyBank but will do so for PyPoll to compare efficiencies
import pandas as pd
pyBank = pd.read_csv('C:\\Users\\Vlad\\colnyc201907data3\\Homework\\03-Python\\Instructions\\PyBank\\Resources\\budget_data.csv')
print()
print("Testing My Code")
print("--------------------------")
print()

TotalMonths = pyBank['Date'].value_counts().sum()
print('Total Months: ', TotalMonths)

NetTotalAmount = pyBank['Profit/Losses'].sum()
print('Net Total Amount: ', '$',NetTotalAmount)

pyBank['ShiftedPL'] = pyBank['Profit/Losses'].shift(1)
pyBank['Difference'] = pyBank['Profit/Losses'] - pyBank['ShiftedPL']

AvgOfChanges = round(pyBank['Difference'].mean(),2)
print('Average Change: ','$',AvgOfChanges)

GreatIncrease = pyBank['Difference'].max()
DateOfIncrease = pyBank[pyBank['Difference'] == GreatIncrease]['Date'].values[0]
GreatestIncrease = print('Greatest Increase in Profits:', DateOfIncrease, GreatIncrease)

GreatDecrease = pyBank['Difference'].min()
DateOfDecrease = pyBank[pyBank['Difference'] == GreatDecrease]['Date'].values[0]
GreatestDecrease = print('Greatest Decrease in Profits:', DateOfDecrease, GreatDecrease)
print()

print('Formatting of Financial Analysis')
print()

print("Financial Analysis")
print("--------------------------")
print('Total Months =' + str(TotalMonths))
print('Net Total Amount =' + '$'+str(NetTotalAmount))
print('Average Change: ' + '$'+str(AvgOfChanges))
print('Greatest Increase in Profits:' + str(DateOfIncrease) + ' ($' + str(int(GreatIncrease)) + ')')
print('Greatest Decrease in Profits:' + str(DateOfDecrease) + ' ($' + str(int(GreatDecrease)) + ')')

with open('C:\\Users\\Vlad\\Documents\\Data Analytics BootCamp\\Python HW\\PyBank\\Vladlen_Suris_FinancialAnalysis.txt','w+') as text_file:
    text_file.write('Financial Analysis')
    text_file.write('\n')
    text_file.write("--------------------------")
    text_file.write('\n')
    text_file.write('Total Months: ' + str(TotalMonths))
    text_file.write('\n')
    text_file.write('Net Total Amount: ' + '$'+str(NetTotalAmount))
    text_file.write('\n')
    text_file.write('Average Change: ' + '$'+str(AvgOfChanges))
    text_file.write('\n')
    text_file.write('Greatest Increase in Profits: ' + str(DateOfIncrease) + ' ($' + str(int(GreatIncrease)) + ')')
    text_file.write('\n')
    text_file.write('Greatest Decrease in Profits: ' + str(DateOfDecrease) + ' ($' + str(int(GreatDecrease)) + ')')