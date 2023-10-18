from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile, User
from django.contrib import messages


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
def home(request, form_error=False):
    # get instance of user profile
    UserProfileInstance = UserProfile.objects.get(user=request.user)

    return render(request, 'homepage/home.html',
        context={
            "form": UserProfileForm(instance=UserProfileInstance),
            "form_error": form_error,
            "username": UserProfileInstance.name,
        }
    )


@login_required
def profileUpdate(request):

    # get the logged in user profile
    UserProfileInstance = UserProfile.objects.get(user=request.user)

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=UserProfileInstance)
        
        form_error = False

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            instance = form.save(commit=False)

            # save the profile object to the user
            instance.user = request.user
            instance.save()
            messages.success(request, "Profile Updated Successfully.")

            # redirect to a new URL:
            return HttpResponseRedirect("/home/")
        
        else:
            form_error = True

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserProfileForm(instance=UserProfileInstance)
        form_error = True
    
    return render(request, 'homepage/home.html', context={"form": form, "form_error": form_error})


# profile view
def profile(request):
     # get instance of user profile
    UserProfileInstance = UserProfile.objects.get(user=request.user)

    form = UserProfileForm(instance=UserProfileInstance)
    return render(request, 'homepage/profile.html', context={"form": form})