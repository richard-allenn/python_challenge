import os
import csv



#locate csv file
csvpath = os.path.join('..', 'resources', 'budget_data.csv')

# open and read the file
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    
    # open and read the file
    file = open('profits_analysis.txt','w')

    # locate the header 
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")


    #define variables
    month_count = 0
    total_profits = 0 
    average_change = 0
    max_profit = 0
    low_profit = 0

    prevmonth_profit = 0
    currentmonth_profit = 0
    months_increase = 0
    max_increase = 0
    max_increase_month = None
    increase_list = []
    
    prevmonth_loss = 0
    currentmonth_profit = 0
    months_loss = 0
    max_loss = 0
    max_loss_month = None
    
    # itterate through the data
    for row in csv_reader:

        # calculate how many months are in the data
        month_count = month_count + 1

        #calculate the total profits                                                       
        total_profits = int(row[1]) + total_profits   

        #calculate the max increase in profit
        currentmonth_profit = int(row[1])
        months_increase = currentmonth_profit - prevmonth_profit
        increase_list.append(months_increase)
        
        if months_increase > max_increase:
            max_increase = months_increase
            max_increase_month = row[0]
        prevmonth_profit = currentmonth_profit      

         #calculate the max decrease in profit
        currentmonth_loss = int(row[1])
        months_loss = currentmonth_loss - prevmonth_loss
        if months_loss < max_loss:
            max_loss = months_loss
            max_loss_month = row[0]
        prevmonth_loss = currentmonth_loss 
    
    average_change = round(sum(increase_list)/ len(increase_list),2)
    


    # open and read the file
    file = open('profits_analysis.txt','w')
    
    file.write('Financial Analysis')
    file.write('\n')
    file.write('----------------------------')
    file.write('\n')
    file.write(f'there is {month_count} months total''\n')
    file.write(f'the total profit/loss is ${total_profits}''\n')
    file.write(f'the average change is ${average_change}''\n')  
    file.write(f'the greatest increase was {max_increase_month} with ${max_increase}''\n')
    file.write(f'the greatest decrease was {max_loss_month} with ${max_loss}''\n')

    
    
    
    
                                             
    
    print()
    print(f'there is {month_count} months total')
    print(f'the total profit/loss is ${total_profits}')
    print(f'the average change is ${average_change}')  
    print(f'the max increase was {max_increase_month} with ${max_increase}')
    print(f'the max decrease was {max_loss_month} with ${max_loss}')
    print()                    
 
    
    
    
 






 

