from django import forms
from django.contrib.auth.models import User
from .models import Company

class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['source_name', 'company_name', 'phone_number', 'address', 'city', 'state', 'zip', 'website']
