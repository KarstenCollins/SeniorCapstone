from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
<<<<<<< Updated upstream
from django.views.generic import ListView, DetailView, CreateView
=======
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )
>>>>>>> Stashed changes
from .models import Post

#from typing import List


#go into home template when you need to change the fields of the db
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'SubmitData/home.html', context)


class PostListView(ListView):
    model = Post #this is what will be queried from models.py
    template_name = 'SubmitData/home.html' #this changes the default template that django wants
    context_object_name = 'posts' #this is what you want the list to display
    ordering = ['-date_entered']#newest to oldest ordering


<<<<<<< Updated upstream
class PostDetailView(DetailView):
    model = Post 
=======

class PostDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Post
>>>>>>> Stashed changes

#CreateView handles all sending to db. It takes from the Post model and the fields are what is shown
class PostCreateView(LoginRequiredMixin, CreateView): #this is the form for entering a bill, Amber's code
    model = Post
    fields = ['title', 'company_name', 'account_number', 'statement_date', 'due_date', 'amount', 'payment_method', 'is_paid', 'previous_balance', 'payments', 'adjustment', 'credits', 'late_fees', 'interest_charges']

    def form_valid(self, form):
        form.instance.author = self.request.user #sets author to logged in user
        return super().form_valid(form)
<<<<<<< Updated upstream
    

def BillStatement(request):
    return render(request, 'SubmitData/billstatement.html', {'title':'About'})

#def income(request):
    #return render(request, 'SubmitData/income.html', {'title':'Income'})

=======

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #this is the form for entering a bill, Amber's code
    model = Post
    fields = ['title', 'company_name', 'account_number', 'statement_date', 'due_date', 'amount', 'payment_method', 'is_paid', 'previous_balance', 'payments','adjustment', 'credits', 'late_fees', 'interest_charges']

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

def BillStatement(request):
    return render(request, 'SubmitData/billstatement.html', {'title':'About'})
>>>>>>> Stashed changes
