from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
# Create your views here.

def pagPrincipal(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'principal/pagPrincipal.html',{'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'principal/post_detail.html', {'post': post})
