from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import BankCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib import messages
from .models import Bank



class BankCreateView(LoginRequiredMixin, CreateView):
    model = Bank
    fields = ['bank_name', 'bank_acc_number', 'nickname', 'account_type', 'routing_number', 'notes']
    context_object_name = 'banks'

    def form_valid(self, form):
        form.instance.user = self.request.user #sets author to logged in user
        return super().form_valid(form)

class BankListView(LoginRequiredMixin, ListView):
    model = Bank
    template_name = 'BankInformation/bank_display.html'
    context_object_name = 'banks'

    def get_queryset(self): #only show logged in users' data
        return self.model.objects.all().filter(user=self.request.user)

class BankUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Bank
    fields = ['bank_name', 'bank_acc_number', 'nickname', 'account_type', 'routing_number', 'notes']
    context_object_name = 'banks'

    def form_valid(self, form):
        form.instance.user = self.request.user #sets author to logged in user
        return super().form_valid(form)

    def test_func(self):
        bank = self.get_object()
        if self.request.user == bank.user:
            return True
        return False

#
class BankDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Bank
    success_url = '/ViewBanks' #home page redirect when finished
    #template_name = 'BankInformation/bank_del_update.html'
    context_object_name = 'banks'

    def test_func(self):
        bank = self.get_object()
        if self.request.user == bank.user:
            return True
        return False

class BankDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Bank

    def test_func(self):
        bank = self.get_object()
        if self.request.user == bank.user:
            return True
        return False
