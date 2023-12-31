from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, BankAccountForm, LoanAccountForm, CreditCardForm, InvestmentAccountForm, TransactionForm
from .models import UserProfile, User, Account, BankAccount, LoanAccount, CreditCard, InvestmentAccount, Category, Transaction
from .utils import currency_symbol, currency_name
from django.urls import reverse
import django_tables2 as tables
from .tables import TransactionTable
from django_tables2 import SingleTableMixin
from django.contrib import messages
from .filters import TransactionFilter
from django_filters.views import FilterView


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
    
    # context for home page
    context={
            "profileform": UserProfileForm(instance=UserProfileInstance),  # profile form for editing when user is logged in and no country and name is set
            "form_error": form_error,   # form error when userprofile is not valid
            "bankForm": BankAccountForm(instance=UserProfileInstance), # bank form for creating new bank accounts
            "loanForm": LoanAccountForm(instance=UserProfileInstance), # loan form for creating new loan accounts
            "creditCardForm": CreditCardForm(instance=UserProfileInstance), # credit card form for creating new credit cards
            "investmentForm": InvestmentAccountForm(instance=UserProfileInstance), # investment form for creating new investment accounts
            "username": UserProfileInstance.name,   # username from user
            "country": str(UserProfileInstance.country), # country from user
            "currency_name": currency_name(str(UserProfileInstance.country)), # currency from user using country name
            "bankAccounts": BankAccount.objects.filter(user=request.user),   # bank accounts associated with user
            "loanAccounts": LoanAccount.objects.filter(user=request.user),   # loan accounts associated with user
            "creditCards": CreditCard.objects.filter(user=request.user),   # credit cards associated with user
            "investmentAccounts": InvestmentAccount.objects.filter(user=request.user),   # investment accounts associated with user
            "transactionForm": TransactionForm(request=request), # expense form
            "alltransactions": Transaction.objects.filter(user=request.user), # expense transactions
        }

    if request.htmx:
        return render(request, 'homepage/home_partial.html', context=context)
    else:
        return render(request, 'homepage/home.html', context=context)

# load categories dropdown using htmx
def htmx_load_categories(request):
    user = request.user # get current user
    tab = request.GET.get('tab')    # get tab from request 
    categories = Category.objects.filter(user=user, category_type=tab)  # get categories based on tab i.e. income and expense
    if request.htmx:
        return render(request, 'homepage/category_dropdown_list_options.html', {'categories': categories})  # render category dropdown list options when using htmx
    else:
        return home(request)

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
            
            # update curreny of all accounts associated with user
            accounts = Account.objects.filter(user=request.user)
            for account in accounts:
                account.currency = currency_name(str(UserProfileInstance.country))
                account.save()
            
            # update currency of all transacations associated with user
            transactions = Transaction.objects.filter(user=request.user)
            for transaction in transactions:
                transaction.currency = currency_name(str(UserProfileInstance.country))
                transaction.save()

            # redirect to a new URL:
            return HttpResponseRedirect("/home/")
        
        else:
            form_error = True

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserProfileForm(instance=UserProfileInstance)
        form_error = True
    
    return render(request, 'homepage/home.html', context={"profileform": form, "form_error": form_error, "username": UserProfileInstance.name})



# create bank account
@login_required
def createBankAccount(request):
    # get instance of current user
    user = User.objects.get(id=request.user.id)
    
    # instance of userProfile of current user
    UserProfileInstance = UserProfile.objects.get(user=request.user)
    
    if request.method == "POST":
        form = BankAccountForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.currency = currency_name(str(UserProfileInstance.country))
            instance.save()
            messages.success(request, "Bank Account Created Successfully.")
            return HttpResponseRedirect("/home/")
    else:
        form = BankAccountForm()
        messages.error(request, "Bank Account Creation Failed.")
        return HttpResponseRedirect("/home/")


# create credit card accounts
@login_required
def createCreditCard(request):
    # get instance of current user
    user = User.objects.get(id=request.user.id)
    
    # instance of userProfile of current user
    UserProfileInstance = UserProfile.objects.get(user=request.user)
    
    if request.method == "POST":
        form = CreditCardForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.currency = currency_name(str(UserProfileInstance.country))
            instance.save()
            messages.success(request, "Credit Card Account Created Successfully.")
            return HttpResponseRedirect("/home/")
    else:
        form = BankAccountForm()
        messages.error(request, "Credit Card Account Creation Failed.")
        return HttpResponseRedirect("/home/")


# create loan accounts
@login_required
def createLoanAccount(request):
    # get instance of current user
    user = User.objects.get(id=request.user.id)
    
    # instance of userProfile of current user
    UserProfileInstance = UserProfile.objects.get(user=request.user)
    
    if request.method == "POST":
        form = LoanAccountForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.currency = currency_name(str(UserProfileInstance.country))
            instance.save()
            messages.success(request, "Loan Account Created Successfully.")
            return HttpResponseRedirect("/home/")
    else:
        form = LoanAccountForm()
        messages.error(request, "Loan Account Creation Failed.")
        return HttpResponseRedirect("/home/")


# create Investment accounts
@login_required
def createInvestmentAccount(request):
    # get instance of current user
    user = User.objects.get(id=request.user.id)
    
    # instance of userProfile of current user
    UserProfileInstance = UserProfile.objects.get(user=request.user)
    
    if request.method == "POST":
        form = InvestmentAccountForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.currency = currency_name(str(UserProfileInstance.country))
            instance.save()
            messages.success(request, "Investment Account Created Successfully.")
            return HttpResponseRedirect("/home/")
    else:
        form = InvestmentAccountForm()
        messages.error(request, "Investment Account Creation Failed.")
        return HttpResponseRedirect("/home/")  


# create or update expense transactions
@login_required
def createTransaction(request):
    if request.method == "POST":

        form = TransactionForm(request.POST, request=request)     

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, "Transaction Saved Successfully.")
            return HttpResponseRedirect("/home/")
        else:
            print(form.errors.as_data())
            messages.error(request, "Transaction Save Failed due to form validation.")
            return HttpResponseRedirect("/home/")
    else:
        form = TransactionForm(request=request)
        messages.error(request, "Expense Transaction Save Failed.")
        return HttpResponseRedirect("/home/")


# All Transactions table view class
class TransactionsHTMxTableView(SingleTableMixin, FilterView):
    table_class = TransactionTable
    queryset = Transaction.objects.all()
    filterset_class = TransactionFilter
    paginate_by = 10

    def get_template_names(self):
        if str(self.request.user) != "AnonymousUser":   # check if user is logged in
            if self.request.htmx:
                template_name = "homepage/alltransactions_partial.html"
            else:
                template_name = "homepage/alltransactions.html"

            return template_name
        else:
            template_name = "chittabook/index.html"
            messages.error(self.request, "Please login to view all transactions.")
            return template_name



# htmx budget function
def htmxBudget(request):
    if request.htmx:
        return render(request, 'homepage/budget_partial.html')
    else:
        return home(request)


# htmx recurring function
def htmxRecurring(request):
    if request.htmx:
        return render(request, 'homepage/recurring_partial.html')
    else:
        return home(request)


# htmx goals function
def htmxGoals(request):
    if request.htmx:
        return render(request, 'homepage/goals_partial.html')
    else:
        return home(request)