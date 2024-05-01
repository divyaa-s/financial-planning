# forms.py
from django import forms

class NewsArticleForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
