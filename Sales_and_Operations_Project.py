
# Sales And Operations Planning Project

"""

>>>Write a Python program that asks the user to enter the following data:

--- An initial stock level for a product
--- The number of month(s) to plan
--- The planned sales quantity for each month

>>>Based on this data, calculate the required production quantity as follows:

--- If the sales quantity is smaller than the stock level of the previous month, the production quantity is 0
--- If the sales quantity is larger than the stock level of the previous month, the production quantity is this difference

"""

# Solution

# create a list for Sales_Qty, Stock_Level & Production_Qty

Sales_Qty = []
Stock_Level = []
Production_Qty = []

#Ask the user for initial stock level
print()
Stock_Level.append(float(input('Please Enter an Initial Stock level: \n')))

#Ask the user for number of Months
print()
Months=int(input('Please Enter the Number of Months to Plan: \n'))


for i in range(0,Months):
#Ask the user for the planned sales qty for each month
    Sales_Qty.append(float(input(f'Please Enter the Planned Sales Quantity for Month {i+1}: \n')))

#Write logic to calculate production qty & stocklevel for each month
    if Sales_Qty[i]<Stock_Level[i]:
        Production_Qty.append(0)
        Stock_Level.append(Stock_Level[i]-Sales_Qty[i])
    else:
        Production_Qty.append(int(Sales_Qty[i]-Stock_Level[i]))
        Stock_Level.append(0)

#Display the resulting production quantities
print()
print('MONTHLY PRODUCTION QUANTITIES \n')

for i in range(0,Months):
    print(f'Month {i+1} - {Production_Qty[i]}')
