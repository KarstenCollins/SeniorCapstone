from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

#go into home template when you need to change the fields of the db
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'SubmitData/home.html', context)

def about(request):
    return render(request, 'SubmitData/about.html', {'title':'About'})