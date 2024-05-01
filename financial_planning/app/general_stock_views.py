# views.py

from django.shortcuts import render
import requests

def stock_prices(request):
    # List of companies and their respective stock symbols
    companies = [
        {"name": "Apple Inc.", "symbol": "AAPL"},
        {"name": "Microsoft Corporation", "symbol": "MSFT"},
        {"name": "Amazon.com Inc.", "symbol": "AMZN"},
        {"name": "Alphabet Inc. (Google)", "symbol": "GOOGL"},
        {"name": "Facebook, Inc.", "symbol": "FB"},
        {"name": "Tesla, Inc.", "symbol": "TSLA"},
        {"name": "NVIDIA Corporation", "symbol": "NVDA"},
        {"name": "Visa Inc.", "symbol": "V"},
        {"name": "JPMorgan Chase & Co.", "symbol": "JPM"},
        {"name": "Johnson & Johnson", "symbol": "JNJ"},
        {"name": "Procter & Gamble Company", "symbol": "PG"},
        {"name": "Walmart Inc.", "symbol": "WMT"},
        # Add more companies as needed
    ]
    
    stock_data = []
    
    for company in companies:
        # Replace YOUR_API_KEY with your actual API key
        api_key = 'DIJ4KF8XY9ME18YO'
        url = f'https://api.example.com/stock/{company["symbol"]}?apikey={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            stock_data.append({
                "name": company["name"],
                "symbol": company["symbol"],
                "price": data["price"],
                # Add more data if needed
            })
    
    context = {
        "stock_data": stock_data
    }
    
    return render(request, 'stocks.html', context)
