from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'chittabook/index.html')


# home page view for chittabook app
@login_required
def home(request):
    return render(request, 'chittabook/home.html')