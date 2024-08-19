from django import forms
from .models import Criminal

class CriminalForm(forms.ModelForm):
    class Meta:
        model = Criminal
        fields = '__all__'

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=100, label='Search')