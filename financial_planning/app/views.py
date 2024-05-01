import os
import csv
import requests
import yfinance as yf
from decimal import Decimal
from datetime import datetime
from django.shortcuts import redirect
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.dateparse import parse_date
from django.http import HttpResponse
from .models import FinancialRecord
from django.http import JsonResponse
from ..useless.recommendations import recommend_schemes
from .utils import read_financial_data_from_csv, fetch_current_stock_price, calculate_investment_amount


user_data=None
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('regUsername')
        raw_password = request.POST.get('regPassword')
        regdate_str = request.POST.get('regDate')
        if not regdate_str:
            return render(request, 'signup.html', {'error': 'Registration date is missing.'})
        try:
            regdate = datetime.strptime(regdate_str, '%d/%m/%Y')
        except ValueError:
            return render(request, 'signup.html', {'error': 'Invalid date format. Please enter the date in DD/MM/YYYY format.'})

        if is_username_unique(username):
            hashed_password = make_password(raw_password)

            with open('users.csv', 'a', newline='') as csvfile:
                fieldnames = ['username', 'password', 'regdate']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                if csvfile.tell() == 0:
                    writer.writeheader()

                writer.writerow({'username': username, 'password': hashed_password, 'regdate': regdate.strftime('%d/%m/%Y')})

            return HttpResponseRedirect(reverse('login'))  # Assuming you have a 'login' URL name
        else:
            return render(request, 'signup.html', {'error': 'Username already exists. Please choose a different username.'})

    else:
        return render(request, 'signup.html')

def is_username_unique(username):
    # Check if username exists in the CSV file
    with open('users.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['username'] == username:
                # If username exists, return False
                return False  # Username already exists
    return True  # Username is unique

def login_view(request):
    global user_data
    if request.method == 'POST':
        # Handle login form submission
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_data = get_user_data(username)
        if user_data:
            hashed_password = user_data['password']
            if check_password(password, hashed_password):
                return HttpResponseRedirect(reverse('dashboard'))  # Assuming 'dashboard' is the URL name for your dashboard page
            else:
                return render(request, 'login.html', {'error': 'Invalid username or password'})
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def get_user_data(username):
    with open('users.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['username'] == username:
                return row
    return None

def check_password(username, password):
    with open('users.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['username'] == username and row['password'] == password:
                return True
    return False

def profile(request):
    # Read users.csv to get the join date and username for the current user
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Update user_name for every row
            user_name = row['username']
            join_date_str = row['regdate']

    # Pass the join date and username to the template context
    return render(request, 'user_profile.html', {'join_date': join_date_str, 'user_name': user_name})

def financial_data(request):
    if request.method == 'POST':
        # Extract financial data and username from POST request
        username = request.POST.get('username')
        income = float(request.POST.get('income', 0))
        food = float(request.POST.get('food', 0))
        transportation = float(request.POST.get('transportation', 0))
        entertainment = float(request.POST.get('entertainment', 0))
        utilities = float(request.POST.get('utilities', 0))
        other = float(request.POST.get('other', 0))
        goal = float(request.POST.get('goal', 0))

        # Calculate total expenses
        total_expenses = food + transportation + entertainment + utilities + other
        
        # Check if total expenses exceed income
        if total_expenses > income:
            # If expenses exceed income, render the form again with an error message
            return render(request, 'calculate.html', {'error_message': "Total expenses cannot exceed income."})

        # Calculate balance
        balance = income - total_expenses
        
        # Save financial data to CSV file
        try:
            with open('financial_data.csv', 'a', newline='') as csvfile:
                fieldnames = ['Username', 'Income', 'Food', 'Transportation', 'Entertainment', 'Utilities', 'Other', 'Total Expenses', 'Balance', 'Goal']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  
                
                # Write headers if the file is empty
                if csvfile.tell() == 0:
                    writer.writeheader()
            
                writer.writerow({
                    'Username': username,
                    'Income': income,
                    'Food': food,
                    'Transportation': transportation,
                    'Entertainment': entertainment,
                    'Utilities': utilities,
                    'Other': other,
                    'Total Expenses': total_expenses,
                    'Balance': balance,
                    'Goal': goal
                })
        except Exception as e:
            # Handle any exceptions that occur during file writing
            return render(request, 'calculate.html', {'error_message': f"An error occurred while saving data: {e}"})
        
        # Redirect to the appropriate URL after processing the data
        return HttpResponseRedirect(reverse('display'))  # Replace 'display' with the correct URL name

    else:
        # Handle GET request (render the form for inputting financial data)
        return render(request, 'calculate.html')

def stocks(request):
    apple = yf.Ticker("AAPL")  # AAPL is the ticker symbol for Apple Inc.
    apple_data = apple.history(period="1y")  # Retrieve one year of historical data
    dates = apple_data.index.strftime('%Y-%m-%d').tolist()
    prices = apple_data['Close'].tolist()
    context = {
        'dates': dates,
        'prices': prices,
    }
    return render(request, 'stocks.html', context)

def microsoft(request):
    microsoft = yf.Ticker("MSFT")  # MSFT is the ticker symbol for Microsoft Corporation
    microsoft_data = microsoft.history(period="1y")  # Retrieve one year of historical data
    dates = microsoft_data.index.strftime('%Y-%m-%d').tolist()
    prices = microsoft_data['Close'].tolist()
    context = {
        'dates': dates,
        'prices': prices,
    }
    return render(request, 'microsoft.html', context)

def google(request):
    google = yf.Ticker("GOOG")  # GOOG is the ticker symbol for Alphabet Inc. (Google)
    google_data = google.history(period="1y")  # Retrieve one year of historical data
    dates = google_data.index.strftime('%Y-%m-%d').tolist()
    prices = google_data['Close'].tolist()
    context = {
        'dates': dates,
        'prices': prices,
    }
    return render(request, 'google.html', context)

def tcs(request):
    tcs = yf.Ticker("TCS.BO")  # TCS.BO is the ticker symbol for Tata Consultancy Services (TCS) in the Bombay Stock Exchange (BSE)
    tcs_data = tcs.history(period="1y")  # Retrieve one year of historical data
    dates = tcs_data.index.strftime('%Y-%m-%d').tolist()
    prices = tcs_data['Close'].tolist()
    context = {
        'dates': dates,
        'prices': prices,
    }
    return render(request, 'tcs.html', context)

def calendar(request):
    return render(request, 'calendar.html')

def financial_summary(request):
    # Read financial data from CSV file
    try:
        with open('financial_data.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            financial_data = list(reader)  # Convert reader to a list
            last_row = financial_data[-1]  # Get the last row
            # Convert values to Decimal for better precision
            for key, value in last_row.items():
                try:
                    last_row[key] = Decimal(value)
                except Exception as e:
                    print(f"Error converting '{value}' to Decimal for key '{key}': {e}")
    except FileNotFoundError:
        # Handle the case where the file does not exist
        last_row = None

    return render(request, 'financial_summary.html', {
        'total_spent': last_row.get('Daily Expenses', 0),
        'available_balance': last_row.get('Balance', 0),
        'last_row': last_row,
    })

def change_password(request):
    if request.method == 'POST':
        # Assuming you have form data with the old password, new password, and confirm password fields
        old_password = request.POST.get('old-password')
        new_password = request.POST.get('new-password')
        confirm_password = request.POST.get('confirm-password')

        # Verify new password matches confirmation
        if new_password != confirm_password:
            # Handle password mismatch error
            return HttpResponse("New password and confirm password do not match")

        # Read users.csv
        with open('users.csv', 'r') as file:
            reader = csv.DictReader(file)
            users = list(reader)

        # Find the user by some identifier, for example, username
        username = request.user.username  # Assuming you have authentication set up
        user_index = None
        for i, user in enumerate(users):
            if user['username'] == username:
                user_index = i
                break

        if user_index is not None:
            # Update the password for the user
            users[user_index]['password'] = new_password

            # Write the updated data back to users.csv
            with open('users.csv', 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=users[0].keys())
                writer.writeheader()
                writer.writerows(users)

            # Handle successful password change
            return HttpResponse("Password changed successfully")

def help(request):
    return render(request, "help.html")

def dashboard_view(request): 
    income = []
    total_expenses = []
    with open('financial_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            income.append(float(row['Income']))
            total_expenses.append(float(row['Daily Expenses']))
    context = {
        'income_data': income,
        'expense_data': total_expenses,
    }

    return render(request, 'dashboard.html', context)

def schemes(request):
    return render(request, 'schemes.html')

from .forms import NewsArticleForm
from textblob import TextBlob
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib


# Define preprocessing function
def preprocess_and_extract_features(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    preprocessed_text = ' '.join(tokens)
    return preprocessed_text

from sklearn.feature_extraction.text import TfidfVectorizer
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.sentiment import SentimentIntensityAnalyzer
from django.shortcuts import render
from .forms import NewsArticleForm

nlp = spacy.load("en_core_web_sm")
sid = SentimentIntensityAnalyzer()

def extract_keywords(text):
    doc = nlp(text)
    entities = [ent.text for ent in doc.ents if ent.label_ in ['ORG', 'PERSON', 'GPE']]
    sentiment_score = sid.polarity_scores(text)
    sentiment = "positive" if sentiment_score['compound'] >= 0 else "negative"
    keywords = entities + [sentiment]
    return keywords[:10]  # Adjust the number of keywords as needed

def analyze_news(request):
    if request.method == 'POST':
        form = NewsArticleForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            keywords = extract_keywords(text)
            preprocessed_text = preprocess_and_extract_features(text)
            vectorizer = TfidfVectorizer()
            features = vectorizer.fit_transform([preprocessed_text])
            return render(request, 'analysis_result.html', {'text': text, 'keywords': keywords})
    else:
        form = NewsArticleForm()
    return render(request, 'input_form.html', {'form': form})


import numpy as np
from sklearn.linear_model import LinearRegression
from .models import Investment
from django.http import HttpResponse
from django.template import loader


def calculate_investment(request):
    if request.method == 'POST':
        goal = float(request.POST.get('goal'))
        current_stock_price = float(request.POST.get('current_stock_price'))
        
        investments = Investment.objects.all()
        print("Number of investments:", len(investments))  # Debugging print
        
        X = [[investment.goal, investment.current_stock_price] for investment in investments]
        y = [investment.investment_amount for investment in investments]
        
        print("X:", X)  # Debugging print
        print("y:", y)  # Debugging print
        
        model = LinearRegression()
        model.fit(X, y)
        
        # Reshape the input data into a 2D array
        input_data = np.array([[goal, current_stock_price]])
        
        # Predict the investment amount
        predicted_investment = model.predict(input_data.reshape(1, -1))
        
        # Redirect to 'stocks.html' with the calculated investment amount as query parameters
        return HttpResponseRedirect(reverse('stocks') + f'?current_stock_price={current_stock_price}&goal={goal}&predicted_investment={predicted_investment[0]}')

    return render(request, 'calculate_investment.html')
