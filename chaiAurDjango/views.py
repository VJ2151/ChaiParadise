from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello Brother! Welcome to Home Page.")
    return render(request, 'website/home.html')

def about(request):
    return HttpResponse("Hello Brother! Welcome to about Page.")

def contact(request):
    return HttpResponse("Hello Brother! Welcome to Contact Page.")

def portfolio(request):
    return render(request, 'Website/portfolio.html')