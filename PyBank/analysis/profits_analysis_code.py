import os
import csv


#locate csv file
csvpath = os.path.join('..', 'resources', 'budget_data.csv')

# open and read the file
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')


    # locate the header 
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")


    #count number of months
    month_count = 0
    
    for row in csv_reader:
        print(row)

        month_count = month_count + 1

    print(f'there is {month_count} months total')

    #total profit / losses
    total_profits = 1                                                        
    for row in csv_reader:
        total_profits = (row[1]) + total_profits                        #row[1] syntax??

    print(f'the total profit/loss is {total_profits} dollars')


    # the average of total changes
    average_change = 0
    average_change = total_profits / month_count
    
    print(f'the average change is {average_change}')

    # greatest increase in profits
    max_profit = 1234
    for row in csv_reader:
        if float(row[1]) > float(max_profit):                                       # again
            max_profit = row[1]                                                     
            print(f' the highest profit month is {max_profit}')


    # the greatest decrease in profits
    low_profit = 4321
    for row in csv_reader:
        if row[1] < low_profit:
            print(row)

    print(f'the lowest profit month is {low_profit}')                       #should be one inside if but is here to show rest of code works
        







 

