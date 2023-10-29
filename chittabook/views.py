from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, BankAccountForm, LoanAccountForm, CreditCardsForm, InvestmentAccountForm, ExpenseForm, IncomeForm
from .models import UserProfile, User, BankAccount, LoanAccount, CreditCards, InvestmentAccount, Expense, Income, ExpenseCategory, ExpenseSubCategory, IncomeCategory, IncomeSubCategory
from django.contrib import messages
from .utils import currency_symbol, currency_name
from django.urls import reverse


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
    # get instance of current user
    user = User.objects.get(id=request.user.id)
    
    # instance of userProfile of current user
    UserProfileInstance = UserProfile.objects.get(user=request.user)

    return render(request, 'homepage/home.html',
        context={
            "form": UserProfileForm(instance=UserProfileInstance),  # profile form for editing when user is logged in and no country and name is set
            "form_error": form_error,   # form error when userprofile is not valid
            "bankForm": BankAccountForm(instance=UserProfileInstance), # bank form for creating new bank accounts
            "loanForm": LoanAccountForm(instance=UserProfileInstance), # loan form for creating new loan accounts
            "creditCardForm": CreditCardsForm(instance=UserProfileInstance), # credit card form for creating new credit cards
            "investmentForm": InvestmentAccountForm(instance=UserProfileInstance), # investment form for creating new investment accounts
            "username": UserProfileInstance.name,   # username from user
            "country": str(UserProfileInstance.country), # country from user
            "currency_name": currency_name(str(UserProfileInstance.country)), # currency from user using country name
            "currency": currency_symbol(str(UserProfileInstance.country)), # currency from user using country name
            "bankAccounts": user.bank_accounts.all(),   # bank accounts associated with user
            "loanAccounts": LoanAccount.objects.filter(user=request.user),   # loan accounts associated with user
            "creditCards": CreditCards.objects.filter(user=request.user),   # credit cards associated with user
            "investmentAccounts": InvestmentAccount.objects.filter(user=request.user),   # investment accounts associated with user
            "expenseForm": ExpenseForm(request=request), # expense form
            "incomeForm": IncomeForm(request=request), # income form
            "expensetransactions": Expense.objects.filter(user=request.user), # expense transactions
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
        messages.error(request, "Bank Account Creation Failed.")
        return HttpResponseRedirect("/home/")

        
# create or update expense transactions
@ login_required
def createExpense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST, request=request)
        print(form)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.account = request.user.bank_accounts.get(id=request.POST['account'])
            instance.user = request.user
            instance.save()
            messages.success(request, "Expense Transaction Saved Successfully.")
            return HttpResponseRedirect("/home/")
        else:
            print(form.errors)
            messages.error(request, "Expense Transaction Save Failed.")
            return HttpResponseRedirect("/home/")
    else:
        form = ExpenseForm(request=request)
        messages.error(request, "Expense Transaction Save Failed.")
        return HttpResponseRedirect("/home/")