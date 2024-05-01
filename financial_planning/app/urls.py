from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('dashboard/', dashboard_view,name='dashboard'),
    path('stocks/', stocks, name="stocks"),
    path('schemes/',schemes,name='schemes'),
    path('calculate/', financial_data, name='calculate'),
    path('display/', financial_summary, name='display'),
    path('calendar/', calendar, name='calendar'),
    path('profile/',profile,name='profile'),
    path('microsoft/',microsoft,name="microsoft"),
    path('google/',google,name="google"),
    path('tcs/',tcs,name="tcs"),
    path('help/',help,name='help'),
    path('input/',analyze_news,name='input_form'),
    path('recommend/', calculate_investment, name='calculate_investment'),

]
