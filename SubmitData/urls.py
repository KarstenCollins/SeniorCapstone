from django.urls import path
<<<<<<< Updated upstream
from .views import PostListView, PostDetailView, PostCreateView
from . import views
    #period is current dir
=======
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    BillStatement,
    PostUpdateView,
    PostDeleteView
)
from BankInformation import views as bank_views
from IncomeInformation import views as income_views
from . import views

>>>>>>> Stashed changes

urlpatterns = [
    path('', PostListView.as_view(), name='Submit-Data'),  #Submit-Data is original
        #'' means home
    path('post/<int:pk>/', PostDetailView.as_view(), name='data-detail'),
                #go to primary key
    path('post/new/', PostCreateView.as_view(), name='create-data'),
<<<<<<< Updated upstream
    path('BillStatement/', views.BillStatement, name='Bill-Statement'),
    #path('Income/'), views.income, name = 'Income'), 
]       

=======
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='update-data'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='delete-data'),
    #Added Code
    path('ViewBanks/', bank_views.BankListView.as_view(), name='view-banks'),
    path('BankInfo/', bank_views.BankCreateView.as_view(), name='create-bank'),
                                            #.as_view() if changed to class based
    path('IncomeInfo/', income_views.IncomeCreateView.as_view(), name='create-income'),
    path('ViewIncome/', income_views.IncomeListView.as_view(), name='view-Income'),
]
>>>>>>> Stashed changes
