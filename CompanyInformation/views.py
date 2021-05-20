from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CompanyCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from .models import Company
from .filters import CompanyFilter


class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    fields = ['source_name', 'company_name', 'phone_number', 'address', 'city', 'state', 'zip', 'website']
    context_object_name = 'company'

    def form_valid(self, form):
        form.instance.user = self.request.user #sets author to logged in user
        return super().form_valid(form)

class CompanyListView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'CompanyInformation/company_display.html'
    context_object_name = 'company'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['companyfilter'] = CompanyFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self): #only show logged in users' data
        return self.model.objects.all().filter(user=self.request.user)
