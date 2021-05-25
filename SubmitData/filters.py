import django_filters
from django_filters import DateFilter
from django_filters.filters import DateFromToRangeFilter, DateRangeFilter
from .models import Post
from django import forms
from django.forms import DateInput


class BillFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'company_name': ['icontains'],
            'payment_method': ['icontains'],
            'date_entered' : ['icontains'],
            'account_number' : ['icontains']
        }

class SummariesFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name="due_date", lookup_expr='gte')
    end_date = DateFilter(field_name="due_date", lookup_expr='lte')
    #due_date = DateRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type':'datetime-local'}))
    date_between = django_filters.DateFromToRangeFilter(label='Date range is in between')
    class Meta:
        model = Post
        fields = ['due_date']
