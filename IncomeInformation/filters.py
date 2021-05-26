from django.forms.widgets import Widget
from django_filters.filters import DateFromToRangeFilter, DateRangeFilter
import django_filters
from django_filters import DateFilter
from django.forms import DateInput
from .models import Income

class IncomeFilter(django_filters.FilterSet):
    greater_than = DateFilter(field_name="date_received", lookup_expr='gte', widget=DateInput(attrs={'type': 'date'}))
    less_than = DateFilter(field_name="date_received", lookup_expr='lte', widget=DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Income
        fields = {
            'source_name': ['icontains'],
        }
