from django.shortcuts import render
from django.http import HttpResponse

def todos(request):
    return HttpResponse("Hello, world. You're at the todos index.")

def index(request): 
    return render(request, 'index.html')
    
