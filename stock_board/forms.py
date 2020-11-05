from django import forms
from .models import StockList


class StockForm(forms.ModelForm):
    class Meta:
        model = StockList
        fields = ('code', 'name')