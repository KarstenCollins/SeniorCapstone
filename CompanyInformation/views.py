from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CompanyCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib import messages
from .models import Company
#from .filters import CompanyFilter


class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    fields = ['company_name', 'phone_number', 'address', 'city', 'state', 'zip', 'website']
    context_object_name = 'company'

    def form_valid(self, form):
        form.instance.user = self.request.user #sets author to logged in user
        return super().form_valid(form)

class CompanyListView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'CompanyInformation/company_display.html'
    context_object_name = 'companys'

    def get_queryset(self): #only show logged in users' data
        return self.model.objects.all().filter(user=self.request.user)

class CompanyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Company
    fields = ['company_name', 'phone_number', 'address', 'city', 'state', 'zip', 'website']
    context_object_name = 'companys'

    def form_valid(self, form):
        form.instance.user = self.request.user #sets author to logged in user
        return super().form_valid(form)

    def test_func(self):
        company = self.get_object()
        if self.request.user == company.user:
            return True
        return False


class CompanyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Company
    success_url = '/ViewCompanys' #home page redirect when finished
    #template_name = 'BankInformation/bank_del_update.html'
    context_object_name = 'companys'

    def test_func(self):
        company = self.get_object()
        if self.request.user == company.user:
            return True
        return False

class CompanyDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Company

    def test_func(self):
        company = self.get_object()
        if self.request.user == company.user:
            return True
        return False
