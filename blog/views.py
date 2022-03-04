from turtle import title
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.filter(title__contains = 'W')
    return render(request, 'blog/post_list.html',{'posts': posts})
