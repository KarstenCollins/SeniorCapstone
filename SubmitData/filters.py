import django_filters
from .models import Post

class BillFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        #fields = '__all__'
        fields = {
            'company_name': ['icontains'],
        }
