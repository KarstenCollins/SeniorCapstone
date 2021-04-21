from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, BillStatement 
from BankInformation import views as bank_views
from . import views
   

urlpatterns = [
    path('', PostListView.as_view(), name='Submit-Data'),  #Submit-Data is original
        #'' means home
    path('post/<int:pk>/', PostDetailView.as_view(), name='data-detail'),
                #go to primary key
    path('post/new/', PostCreateView.as_view(), name='create-data'),
    path('ViewBanks/', bank_views.BankListView.as_view(), name='view-banks'),
    path('BankInfo/', bank_views.BankCreateView.as_view(), name='create-bank'),
                                            #.as_view() if changed to class based
]       

