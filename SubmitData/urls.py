from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from . import views
    #period is current dir

urlpatterns = [
    path('', PostListView.as_view(), name='Submit-Data'),  #Submit-Data is original
        #'' means home
    path('post/<int:pk>/', PostDetailView.as_view(), name='data-detail'),
                #go to primary key
    path('post/new/', PostCreateView.as_view(), name='create-data'),
    path('BillStatement/', views.BillStatement, name='Bill-Statement'),
    #path('Income/'), views.income, name = 'Income'), 
]       

