import django_filters
from django_filters import DateFilter
from .models import Post


class BillFilter(django_filters.FilterSet):
    #start_date = DateFilter(field_name="due_date", lookup_expr='gte')
    #end_date = DateFilter(field_name="due_date", lookup_expr='lte')
    class Meta:
        model = Post
        #fields = '__all__'
        fields = {
            'company_name': ['icontains'],
        }

class SummariesFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="due_date", lookup_expr='gte')
    end_date = DateFilter(field_name="due_date", lookup_expr='lte')
    class Meta:
        model = Post
        fields = {
            'due_date':['icontains'],
        }
