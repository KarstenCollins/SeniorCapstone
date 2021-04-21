from django import forms
from django.contrib.auth.models import User
from .models import Bank

class BankCreateForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['bank_name', 'bank_acc_number', 'nickname', 'account_type', 'routing_number', 'notes']