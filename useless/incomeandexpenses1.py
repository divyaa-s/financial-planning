import csv
import os
from datetime import datetime

def initialize_csv_file(csv_filename):
    if not os.path.exists(csv_filename):
        with open(csv_filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Income", "Food", "Transportation", "Entertainment", "Utilities", "Other", "Daily Expenses", "Balance"])

def calculate_daily_expenses(food, transportation, entertainment, utilities, other):
    return food + transportation + entertainment + utilities + other

def calculate_balance(income, daily_expenses):
    return income - daily_expenses

def add_data_to_csv(csv_filename, income, food, transportation, entertainment, utilities, other, daily_expenses, balance, date):
    with open(csv_filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, income, food, transportation, entertainment, utilities, other, '{:.2f}'.format(daily_expenses), '{:.2f}'.format(balance)])

def main():
    csv_filename = "financial_data.csv"
    initialize_csv_file(csv_filename)
    
    income = float(input("Enter your income: "))
    categories = ["Food", "Transportation", "Entertainment", "Utilities", "Other"]
    print("Available categories:", ", ".join(categories))
    chosen_categories = input("Enter the categories you spent in (comma-separated): ").split(',')
    expenses = input("Enter the amounts spent for each category (comma-separated): ").split(',')

    category_expenses = {
        "food": 0,
        "transportation": 0,
        "entertainment": 0,
        "utilities": 0,
        "other": 0
    }

    for category, expense in zip(chosen_categories, expenses):
        category = category.strip().lower()
        if category in category_expenses:
            category_expenses[category] += float(expense)

    daily_expenses = calculate_daily_expenses(category_expenses["food"], category_expenses["transportation"], category_expenses["entertainment"], category_expenses["utilities"], category_expenses["other"])
    
    # Input date in dd/mm/yyyy format
    date = input("Enter date (DD/MM/YYYY): ")
    try:
        date = datetime.strptime(date, "%d/%m/%Y").strftime("%d/%m/%Y")
    except ValueError:
        print("Invalid date format. Please enter date in DD/MM/YYYY format.")
        return

    print("Your total daily expenses:", daily_expenses)
    
    balance = calculate_balance(income, daily_expenses)
    print("Your balance amount:", balance)
    
    add_data_to_csv(csv_filename, income, category_expenses["food"], category_expenses["transportation"], category_expenses["entertainment"], category_expenses["utilities"], category_expenses["other"], daily_expenses, balance, date)

if __name__ == "__main__":
    main()
