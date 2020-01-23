from django.shortcuts import render
# Create your views here.

def pagAbout(request):
    return render(request,'pagAbout.html',{})