from django.urls import include, path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    BillStatement,
    PostUpdateView,
    PostDeleteView,
    BillExport, 
)
from BankInformation import views as bank_views
from IncomeInformation import views as income_views
from CompanyInformation import views as company_views
from . import views as data_views
from cal import views as cal_views

urlpatterns = [
    path('', PostListView.as_view(), name='Submit-Data'), 
        
    path('post/<int:pk>/', PostDetailView.as_view(), name='data-detail'),
    path('post/new/', PostCreateView.as_view(), name='create-data'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='update-data'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='delete-data'),
    path('DownloadBills', BillExport, name='download-bills'),

    path('ViewBanks/', bank_views.BankListView.as_view(), name='view-banks'),
    path('bank/<int:pk>/delete/', bank_views.BankDeleteView.as_view(), name='delete-bank'),
    path('bank/<int:pk>/update/', bank_views.BankUpdateView.as_view(), name='update-bank'),
    path('BankInfo/', bank_views.BankCreateView.as_view(), name='create-bank'),
    path('bank/<int:pk>/', bank_views.BankDetailView.as_view(), name='bank-detail'),
                                            

    path('ViewIncome/', income_views.IncomeListView.as_view(), name='view-incomes'),
    path('income/<int:pk>/delete/', income_views.IncomeDeleteView.as_view(), name='delete-income'),
    path('income/<int:pk>/update/', income_views.IncomeUpdateView.as_view(), name='update-income'),
    path('IncomeInfo/', income_views.IncomeCreateView.as_view(), name='create-income'),
    path('income/<int:pk>/', income_views.IncomeDetailView.as_view(), name='income-detail'),

    path('CompanyInfo/', company_views.CompanyCreateView.as_view(), name='create-company'),
    path('CompanyIncome/', company_views.CompanyListView.as_view(), name='view-company'),
    path('ViewCompanys/', company_views.CompanyListView.as_view(), name='view-companys'),
     path('company/<int:pk>/', company_views.CompanyDetailView.as_view(), name='company-detail'),
    path('company/<int:pk>/delete/', company_views.CompanyDeleteView.as_view(), name='delete-company'),
    path('company/<int:pk>/update/', company_views.CompanyUpdateView.as_view(), name='update-company'),

    path('BillsNotPaid/', data_views.IsPaidView.as_view(), name='is-paid'),
    path('Summaries/', data_views.YearlyMonthlySummaryView.as_view(), name='view-summaries'),

    path(r'index/', cal_views.index, name='index'),
    path(r'calendar/', cal_views.CalendarView.as_view(), name='calendar'),
    path(r'event/new/', cal_views.event, name='event_new'),
	path(r'event/edit/(<event_id>\d+)/', cal_views.event, name='event_edit'),
    #path('event/<int:pk>/remove', cal_views.EventDeleteView.as_view(), name='remove_event'),
    path(r'listcalendar/', cal_views.event_list_view, name='list-calendar'),
    path(r'event/delete/<id>', cal_views.event_delete_view, name='event-delete'),
]
