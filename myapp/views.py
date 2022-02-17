from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')
    
# Create your views here.
