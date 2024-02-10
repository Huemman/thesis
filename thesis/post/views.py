from django.shortcuts import render
from django.views import generic
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

