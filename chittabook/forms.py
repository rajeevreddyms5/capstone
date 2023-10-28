from django.forms import ModelForm, widgets, ValidationError, ChoiceField, ModelChoiceField
from chittabook.models.userprofile import UserProfile
from django_countries.widgets import CountrySelectWidget
from bootstrap_datepicker_plus.widgets import DatePickerInput, DateTimePickerInput
from datetime import date
from chittabook.models.accounts import BankAccount, LoanAccount, CreditCards, InvestmentAccount
from chittabook.models.expense import Expense, ExpenseCategory, ExpenseSubCategory
from chittabook.models.income import Income, IncomeCategory, IncomeSubCategory
from django.utils.html import format_html


# Create your custom views here.


# create userprofile model form
class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'dob', 'profession', 'gender', 'country']
        widgets = {
            'dob': DatePickerInput(),
            'country': CountrySelectWidget(),
        }

    # custom validation for dob
    def clean(self):
        cleaned_data = super().clean()
        dob = cleaned_data.get("dob")

        if dob > date.today():
            raise ValidationError("Date of Birth cannot be in the future.")
        elif dob == date.today():
            raise ValidationError("Date of Birth cannot be today.")
        
        # dob cannot be less than 13 years old
        today = date.today()
        age = int(today.year) - int(dob.year) - ((int(today.month), int(today.day)) < (int(dob.month), int(dob.day)))

        if int(age) < 18:
            raise ValidationError("Date of Birth cannot be less than 13 years.")
        elif int(age) > 100:
            raise ValidationError("Date of Birth cannot be greater than 100 years.")
        
        return cleaned_data




# Bank Account form
class BankAccountForm(ModelForm):
    class Meta:
        model = BankAccount
        fields = ['account_name', 'balance']


# Loan Account form
class LoanAccountForm(ModelForm):
    class Meta:
        model = LoanAccount
        fields = ['lender_name', 'amount', 'balance']


# Credit Cards form
class CreditCardsForm(ModelForm):
    class Meta:
        model = CreditCards
        fields = ['card_name', 'credit_limit', 'initial_debt']



# Investment Account form
class InvestmentAccountForm(ModelForm):
    class Meta:
        model = InvestmentAccount
        fields = ['account_name', 'current_value']


# Expense form with list of accounts to choose from bank account, loan account, credit cards, and investment account
#  and add expense category field to choose from expense categories
class ExpenseForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.fields['account'].choices = self.get_account_choices()
        self.fields['category'].queryset = ExpenseCategory.objects.filter(user=self.request.user).order_by('name')
        
        # add subcategory field to the category field
        choices = []
        categories = self.fields['category'].queryset
        subcategories = ExpenseSubCategory.objects.filter(user=self.request.user)
        for category in categories:
            subcategories_for_category = subcategories.filter(category=category)
            choices.append((category.id, format_html('<strong>{}</strong>', category.name)))
            choices.extend([(subcategory.id, format_html('&nbsp;&nbsp;&nbsp;{}', subcategory.name)) for subcategory in subcategories_for_category])

        self.fields['category'].widget.choices = choices
    
    account = ChoiceField(choices=[], required=True, label='Select Account')
    category = ModelChoiceField(queryset=ExpenseCategory.objects.none())
    
    
    class Meta:
        model = Expense
        fields = ['account', 'amount', 'date', 'note', 'category']
        widgets = {
            'date': DatePickerInput(),
        }

    # Account choices function
    def get_account_choices(self):
        bank_accounts = BankAccount.objects.filter(user=self.request.user)
        credit_cards = CreditCards.objects.filter(user=self.request.user)
        loan_accounts = LoanAccount.objects.filter(user=self.request.user)
        investment_accounts = InvestmentAccount.objects.filter(user=self.request.user)

        account_choices = []

        if bank_accounts:
            account_choices.append(('Bank Accounts', [(a.id, a.account_name) for a in bank_accounts]))

        if credit_cards:
            account_choices.append(('Credit Cards', [(a.id, a.card_name) for a in credit_cards]))

        if loan_accounts:
            account_choices.append(('Loan Accounts', [(a.id, a.account_name) for a in loan_accounts]))

        if investment_accounts:
            account_choices.append(('Investment Accounts', [(a.id, a.account_name) for a in investment_accounts]))

        return account_choices
    
    # Category choices function
    def get_category_choices(self):
        expense_categories = ExpenseCategory.objects.filter(user=self.request.user)
        subcategories = ExpenseSubCategory.objects.filter(user=self.request.user)

        category_choices = []

        for category in expense_categories:
            subcategory_choices = []
            for subcategory in subcategories.filter(category=category):
                subcategory_choices.append((subcategory.id, subcategory.name))
            category_choices.append((category.id, category.name))

        return category_choices


# Income form
