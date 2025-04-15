from django import forms

CHOICES = [
    ('csv', 'csv'),
]

class FormatForm(forms.Form):
    format = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

class SearchMeal(forms.Form):
    datetime = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))