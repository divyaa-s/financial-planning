import csv

def display_spent_and_balance(csv_filename):
    total_spent = 0
    income = None
    with open(csv_filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if income is None:
                income = float(row['Income'])
            total_spent += float(row['Daily Expenses'])
    available_balance = income - total_spent
    print("Total amount spent:", total_spent)
    print("Available balance:", available_balance)

# Example usage:
csv_filename = "financial_data.csv"
display_spent_and_balance(csv_filename)
