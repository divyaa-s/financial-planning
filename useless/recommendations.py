def recommend_schemes(income_balance):
    if income_balance < 1000:
        return ["Savings Account", "Fixed Deposit"]
    elif 1000 <= income_balance < 5000:
        return ["Mutual Funds", "Index Funds"]
    elif income_balance >= 5000:
        return ["Stocks", "ETFs", "Real Estate Investment Trusts (REITs)"]
    else:
        return ["No schemes recommended"]
