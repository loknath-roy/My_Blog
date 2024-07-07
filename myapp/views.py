from django.shortcuts import render
from .models import Catagory,Post

# Create your views here.
def Home(request):
    posts = Post.objects.all()
    cats = Catagory.objects.all()
    return render(request,'home.html',{'posts':posts,'cats': cats})
   
def Posts(request,url):
    post = Post.objects.get(url=url)
    cats = Catagory.objects.all()
    return render(request,'post.html',{'post': post,'cats': cats})

def Catagories(request,url):
    cat = Catagory.objects.get(url=url)
    post = Post.objects.filter(cat=cat)
    cats = Catagory.objects.all()
    # print(cats)
    # print(post)
    return render(request,'catagory.html',{'cat': cat,'post':post,'cats':cats})
