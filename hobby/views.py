from django.shortcuts import render

# Create your views here.

def pagHobby(request):
    return render(request,'hobby/pagHobby.html')