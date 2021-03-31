from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author':'Karsten',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'June 11, 2020'
    }, 
    {'author':'Owen',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'June 12, 2020'
    }
]




def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'SubmitData/home.html', context)

def about(request):
    return render(request, 'SubmitData/about.html', {'title':'About'})