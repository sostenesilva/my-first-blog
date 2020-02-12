from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.

def pagPrincipal(request):
    posts_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    paginator = Paginator(posts_list, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'principal/pagPrincipal.html',{'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'principal/post_detail.html', {'post': post})
