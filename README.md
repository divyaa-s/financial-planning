# Financial Planning & Analytics Tool 📈

A comprehensive Django-based platform designed to help users manage their finances, track investments, and analyze market trends. This tool combines traditional expense tracking with modern Machine Learning and NLP to provide actionable financial insights.

## 🚀 Overview

The **Financial Planning & Analytics Tool** is a one-stop solution for personal finance management. It allows users to track their income and expenses, monitor real-time stock prices, analyze financial news sentiment, and even predict future investment requirements using linear regression models.

## ✨ Key Features

- **User Authentication**: Secure signup and login system with personalized user profiles.
- **Expense Tracking**: Comprehensive dashboard to log income and categorize expenses (Food, Transportation, Entertainment, Utilities, etc.).
- **Real-time Stock Monitoring**: Integration with `yfinance` to track live prices for major stocks like Apple, Microsoft, Google, and TCS.
- **Investment Prediction**: A Machine Learning module using **Linear Regression** to estimate required investment amounts based on financial goals and current market prices.
- **News Sentiment Analysis**: An NLP-powered news analyzer that extracts keywords and determines the sentiment (Positive/Negative) of financial articles using `TextBlob` and `SpaCy`.
- **Financial Summary**: Automated generation of financial summaries showing balance, total spent, and savings progress.
- **Interactive Dashboard**: Visual representation of financial data for better decision-making.

## 🛠️ Technology Stack

- **Backend**: Python 3.x, Django 4.x
- **Data Storage**: CSV-based storage (for lightweight demo) / SQLite
- **Machine Learning**: Scikit-learn (Linear Regression)
- **Natural Language Processing**: SpaCy, NLTK, TextBlob
- **Financial APIs**: Yahoo Finance (`yfinance`), AlphaVantage
- **Frontend**: HTML5, CSS3, Vanilla JavaScript

## 📁 Project Structure

```text
financial_planning/
├── app/
│   ├── models.py          # Database/Data structures for records and investments
│   ├── views.py           # Core logic for stocks, NLP, and ML predictions
│   ├── utils.py           # API integration and calculation utilities
│   ├── templates/         # UI components (Dashboard, Stocks, Analysis)
│   └── static/            # CSS and JS assets
├── financial_planning/    # Project settings and URL routing
├── users.csv              # User credentials storage
├── financial_data.csv     # Financial records storage
└── manage.py              # Django CLI
```

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/financial-planning.git
   cd financial-planning
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

3. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Start the Server**:
   ```bash
   python manage.py runserver
   ```
   Access the app at `http://127.0.0.1:8000/`.

## 📊 Future Roadmap

- [ ] Transition from CSV storage to PostgreSQL for better scalability.
- [ ] Integration of more complex ML models (Random Forest/XGBoost) for stock prediction.
- [ ] Multi-currency support.
- [ ] PDF Export for financial reports.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---
*Developed for financial literacy and data-driven planning.*
