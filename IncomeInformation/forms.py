from django import forms
from django.contrib.auth.models import User
from .models import Income

class IncomeCreateForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['source_name', 'amount', 'date_received']
