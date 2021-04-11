from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


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
    ordering = ['-date_posted']#newest to oldest ordering


class PostDetailView(DetailView):
    model = Post 

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user #sets author to logged in user
        return super().form_valid(form)
    

def BillStatement(request):
    return render(request, 'SubmitData/about.html', {'title':'About'})

#def income(request):
    #return render(request, 'SubmitData/income.html', {'title':'Income'})

