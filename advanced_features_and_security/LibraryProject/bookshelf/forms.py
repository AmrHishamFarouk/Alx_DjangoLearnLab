# bookshelf/forms.py

from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label="Search for a book")
ExampleForm