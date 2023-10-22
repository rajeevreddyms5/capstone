from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, BankAccountForm
from .models import UserProfile, User, BankAccount, LoanAccount, CreditCards, InvestmentAccount
from django.contrib import messages
from .utils import currency_symbol


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
            "bankForm": BankAccountForm(instance=UserProfileInstance), # bank form for creating new bank accounts
            "username": UserProfileInstance.name,
            "country": UserProfileInstance.country,
            "currency": currency_symbol(str(UserProfileInstance.country)),
            "BankAccount": BankAccount.objects.filter(user=request.user),
            "LoanAccount": LoanAccount.objects.filter(user=request.user),
            "CreditCards": CreditCards.objects.filter(user=request.user),
            "InvestmentAccount": InvestmentAccount.objects.filter(user=request.user),
        }
    )


# profile update
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
    
    return render(request, 'homepage/home.html', context={"form": form, "form_error": form_error, "username": UserProfileInstance.name})



# create bank account
@ login_required
def createBankAccount(request):
    if request.method == "POST":
        form = BankAccountForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, "Bank Account Created Successfully.")
            return HttpResponseRedirect("/home/")
    else:
        form = BankAccountForm()