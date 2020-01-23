from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.

def pagHobby(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'hobby/pagHobby.html',{'posts': posts})