from django.shortcuts import render
from .models import Catagory,Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    cats = Catagory.objects.all()
    return render(request,'home.html',{'posts':posts,'cats': cats})
   
def Posts(request,url):
    post = Post.objects.get(url=url)
    cats = Catagory.objects.all()
    return render(request,'post.html',{'post': post,'cats': cats})

def Catagories(request,url):
    cats = Catagory.objects.get(url=url)
    post = Post.objects.filter(cats=cats)
    print(cats)
    print(post)
    return render(request,'catagory.html',{'cats': cats,'post':post})
