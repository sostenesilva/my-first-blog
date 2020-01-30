from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.

def pagPrincipal(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'principal/pagPrincipal.html',{'posts': posts})