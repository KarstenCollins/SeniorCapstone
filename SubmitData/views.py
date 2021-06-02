import csv, io 
from django.shortcuts import render
from django.db.models import Q
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )

import django_filters
from django_filters import DateFilter
from django_filters.filters import DateFromToRangeFilter, DateRangeFilter

from .models import Post
from .filters import BillFilter, SummariesFilter
from .forms import PostForm


#go into home template when you need to change the fields of the db
def home(request):
    myFilter = BillFilter()

    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'SubmitData/home.html', context)


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'SubmitData/home.html'
    context_object_name = 'posts'
    #ordering = ['-date_entered']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = BillFilter(self.request.GET, queryset=self.get_queryset())
        return context


    def get_queryset(self):#only show logged in users' data
        #return self.model.objects.all().filter(author=self.request.user, is_paid=True)
        return self.model.objects.all().filter(author=self.request.user).order_by('-due_date')


class PostDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

#CreateView handles all sending to db. It takes from the Post model and the fields are what is shown
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    #fields = ['title', 'company_name', 'account_number', 'statement_date', 'due_date', 'amount', 'payment_method', 
    #'is_paid', 'payment_method', 'is_paid', 'previous_balance', 'minimum_payment', 'payments', 'adjustment', 
    #'credit', 'late_fees', 'interest_charges']
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user #sets author to logged in user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    #fields = ['title', 'company_name', 'account_number', 'statement_date', 'due_date', 'amount', 'payment_method',  
    #'is_paid', 'payment_method', 'is_paid', 'previous_balance','minimum_payment', 'payments', 'adjustment', 
    # 'credit', 'late_fees', 'interest_charges']
    

    def form_valid(self, form):
        form.instance.author = self.request.user #sets author to logged in user
        return super().form_valid(form)

    #the function that UserPassesTestMixin uses to stop them from updating posts that are not theirs
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' #home page redirect when finished

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class IsPaidView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'SubmitData/not_paid.html'
    context_object_name = 'posts'
    ordering = ['-date_entered']


    def get_queryset(self):#only show logged in users' data
        #return self.model.objects.all().filter(Q(author=self.request.user, due_date__gte=datetime.date.today(), is_paid=False) | Q(author=self.request.user, is_paid=False)) #is_paid=False,
        return self.model.objects.all().filter(Q(author=self.request.user, due_date__gte=datetime.date.today(), is_paid=False)| Q(author=self.request.user, is_paid=False)) #| Q(author=self.request.user, is_paid=False))


class YearlyMonthlySummaryView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'SubmitData/summaries.html'
    context_object_name = 'posts'
    ordering = ['-due_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['summary'] = SummariesFilter(self.request.GET, queryset=self.get_queryset())
        return context

def BillStatement(request):
    return render(request, 'SubmitData/billstatement.html', {'title':'About'})

def BillExport(request):

    items = Post.objects.all().filter(author=request.user)
    #export_user = Post.objects.filter(author=request.user)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="billable_bill_data.csv"'

    writer = csv.writer(response, delimiter=',')
    writer.writerow(['title', 'company_name', 'account_number', 'statement_date', 'due_date', 'date_entered', 
    'amount', 'is_paid', 'payment_method', 'previous_balance', 'minimum_payment', 'payments', 'credit', 'adjustment',
    'late_fees', 'interest_charges'])

    for obj in items:
        writer.writerow([obj.title, obj.company_name, obj.account_number, obj.statement_date, obj.due_date, obj.date_entered, 
    obj.amount, obj.is_paid, obj.payment_method, obj.previous_balance, obj.minimum_payment, obj.payments, obj.credit, obj.adjustment,
    obj.late_fees, obj.interest_charges])

    return response