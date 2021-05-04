import django_filters
from .models import Post

class BillFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        #fields = ['company_name']
        fields = '__all__'
