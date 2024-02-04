import csv

def finance_manager(file):
    total_sum = 0 
    transactions = []

    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        
        for row in csv_reader:
            # Get name, amount, date from the appropriate columns in the CSV
            date = row[0]
            name = row[2]
            debit = row[3]
            credit = row[4]
            
            # Convert debit and credit values to float (handle empty cells)
            if debit:
                amount = -float(debit)
            elif credit:
                amount = float(credit)
            else:
                amount = 0.0
 
            transaction = (date, name, amount)
            total_sum += amount
            transactions.append(transaction)
            
    print(f"The sum of your transactions in this file is {total_sum:.2f}\n")
    return transactions

# Replace 'next_file.csv' with the actual name of the CSV file
next_file = 'july.csv'
transactions = finance_manager(next_file)

for i in range(len(transactions)):
    print(transactions[i])
