from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile


# Create your views here.
def index(request):
    return render(request, 'chittabook/index.html')


# about page view for chittabook app
def about(request):
    return render(request, 'chittabook/about.html')


# contact page view for chittabook app
def contact(request):
    return render(request, 'chittabook/contact.html')

# features page view for chittabook app
def features(request):
    return render(request, 'chittabook/features.html')

# how page view for chittabook app
def how(request):
    return render(request, 'chittabook/how.html')

# privacy page view for chittabook app
def privacy(request):
    return render(request, 'chittabook/privacy.html')

# terms and conditions page view for chittabook app
def terms(request):
    return render(request, 'chittabook/terms.html')



''' home page view for chittabook app starts here'''



# home page view for chittabook app
@login_required
def home(request):
    return render(request, 'homepage/home.html',
        context={
            "form": UserProfileForm,
        }
    )


@login_required
def profileUpdate(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = UserProfileForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form = UserProfileForm(request.POST)
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect("/home/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserProfileForm()

    return render(request, "homepage/home.html", {"form": form})