import django_filters
from django_filters import DateFilter
from .models import Income

class IncomeFilter(django_filters.FilterSet):
    greater_than = DateFilter(field_name="date_received", lookup_expr='gte')
    less_than = DateFilter(field_name="date_received", lookup_expr='lte')
    class Meta:
        model = Income
        fields = {
            'source_name': ['icontains'],
        }
