from django.shortcuts import render
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
from .models import Post
from .filters import BillFilter


#go into home template when you need to change the fields of the db
def home(request):
    myFilter = BillFilter()

    context = {
        'posts': Post.objects.all(),
        'myFilter': myFilter,
    }
    return render(request, 'SubmitData/home.html', context)


class PostListView(LoginRequiredMixin, ListView):
    model = Post 
    template_name = 'SubmitData/home.html' 
    context_object_name = 'posts' 
    ordering = ['-date_entered']


    def get_queryset(self):#only show logged in users' data
        #return self.model.objects.all().filter(author=self.request.user, is_paid=True)
        return self.model.objects.all().filter(author=self.request.user)


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
    fields = ['title', 'company_name', 'account_number', 'statement_date', 'due_date', 'amount', 'payment_method', 'is_paid']

    def form_valid(self, form):
        form.instance.author = self.request.user #sets author to logged in user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Post
    fields = ['title', 'company_name', 'account_number', 'statement_date', 'due_date', 'amount', 'payment_method', 'is_paid']

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
        return self.model.objects.all().filter(author=self.request.user, is_paid=False)

def BillStatement(request):
    return render(request, 'SubmitData/billstatement.html', {'title':'About'})



