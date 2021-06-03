from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.widgets import Widget

from .models import Post

class DateInput(forms.DateInput):
    input_type='date'


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'company_name', 'account_number', 'statement_date', 'due_date', 
        'amount', 'payment_method', 'is_paid']
        widgets = {
            'statement_date' : DateInput(),
            'due_date' : DateInput(),
        }


#'payment_method', 'is_paid', 'previous_balance','minimum_payment', 'payments', 'adjustment', 'credit', 'late_fees', 'interest_charges'
