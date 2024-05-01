import csv
from django.shortcuts import render
import csv

import requests

def read_financial_data_from_csv(csv_file):
    financial_data = []
    with open('financial_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            financial_data.append((row['username'], float(row['income']), float(row['goal']), float(row['balance'])))
    return financial_data

def fetch_current_stock_price(stock_symbol, api_key):
    api_key = 'LMSX1WRpGX40xrD3RbgaPqliZNF1LZn5'
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_symbol}&apikey={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        # Extract the current price from the response
        current_price = float(data['Global Quote']['05. price'])
        return current_price
    except Exception as e:
        print("Error fetching stock price:", str(e))
        return None

def calculate_investment_amount(income, goal, current_stock_price):
    difference = goal - income
    recommended_investment = difference / current_stock_price
    return recommended_investment
