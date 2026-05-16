from django.shortcuts import render
import yfinance as yf

def display_real_time_stock(request):
    symbol = request.GET.get('symbol', 'AAPL')  # Default symbol is AAPL if not provided
    stock = yf.Ticker(symbol)
    try:
        data = stock.history(period="1d")
        latest_data = data.tail(1)
        context = {
            'symbol': symbol,
            'price': latest_data['Close'].values[0],
            'volume': latest_data['Volume'].values[0],
            'open': latest_data['Open'].values[0],
            'high': latest_data['High'].values[0],
            'low': latest_data['Low'].values[0],
            'time': latest_data.index[0]
        }
    except Exception as e:
        context = {'error': str(e)}
    
    return render(request, 'stocks/real_time_stock.html', context)
