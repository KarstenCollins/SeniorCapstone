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
            'company_name': ['icontains'],
        }

class SummariesFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name="due_date", lookup_expr='gte')
    end_date = DateFilter(field_name="due_date", lookup_expr='lte')
    #due_date = DateRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type':'datetime-local'}))
    class Meta:
        model = Post
        fields = ['due_date']
