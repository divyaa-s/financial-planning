# models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db import models

class FinancialRecord(models.Model):
    username = models.CharField(max_length=100)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    food = models.DecimalField(max_digits=10, decimal_places=2)
    transportation = models.DecimalField(max_digits=10, decimal_places=2)
    entertainment = models.DecimalField(max_digits=10, decimal_places=2)
    utilities = models.DecimalField(max_digits=10, decimal_places=2)
    other = models.DecimalField(max_digits=10, decimal_places=2)
    total_expenses = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

from django.db import models

class Investment(models.Model):
    goal = models.CharField(max_length=100)
    current_stock_price = models.DecimalField(max_digits=10, decimal_places=2)
    investment_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Investment: {self.goal} - Price: {self.current_stock_price} - Amount: {self.investment_amount}"
