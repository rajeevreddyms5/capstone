from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'chittabook/index.html')


# home page view for chittabook app
def home(request):
    return render(request, 'chittabook/home.html')