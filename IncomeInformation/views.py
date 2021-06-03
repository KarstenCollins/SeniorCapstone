from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import IncomeCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib import messages

from .models import Income
from .filters import IncomeFilter
from .forms import IncomeForm



class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = Income
    #fields = ['source_name', 'amount', 'date_received']
    form_class = IncomeForm
    context_object_name = 'income'

    def form_valid(self, form):
        form.instance.user = self.request.user #sets author to logged in user
        return super().form_valid(form)

class IncomeListView(LoginRequiredMixin, ListView):
    model = Income
    template_name = 'IncomeInformation/income_display.html'
    context_object_name = 'income'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['incomefilter'] = IncomeFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self): #only show logged in users' data
        return self.model.objects.all().filter(user=self.request.user)

class IncomeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Income
    fields = ['source_name', 'amount', 'date_received']
    context_object_name = 'incomes'

    def form_valid(self, form):
        form.instance.user = self.request.user #sets author to logged in user
        return super().form_valid(form)

    def test_func(self):
        income = self.get_object()
        if self.request.user == income.user:
            return True
        return False


class IncomeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Income
    success_url = '/ViewIncome' #home page redirect when finished
    #template_name = 'BankInformation/bank_del_update.html'
    context_object_name = 'incomes'

    def test_func(self):
        income = self.get_object()
        if self.request.user == income.user:
            return True
        return False

class IncomeDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Income

    def test_func(self):
        income = self.get_object()
        if self.request.user == income.user:
            return True
        return False