from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms import widgets
from django.forms.widgets import Widget
from .models import Income

class IncomeCreateForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['source_name', 'amount', 'date_received']


class DateInput(forms.DateInput):
    input_type='date'


class IncomeForm(ModelForm):

    class Meta:
        model = Income
        fields = ['source_name', 'amount', 'date_received']
        widgets = {
            'date_received' : DateInput(),
        }
