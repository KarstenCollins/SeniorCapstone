from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import IncomeCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from .models import Income
from .filters import IncomeFilter




class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = Income
    fields = ['source_name', 'amount', 'date_received']
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

