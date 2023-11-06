from django.forms import ModelForm, widgets, ValidationError, ChoiceField, ModelChoiceField, DateInput, TextInput
from chittabook.models.userprofile import UserProfile
from django_countries.widgets import CountrySelectWidget
from bootstrap_datepicker_plus.widgets import DatePickerInput, DateTimePickerInput
from datetime import date
import datetime
from chittabook.models.accounts import BankAccount, LoanAccount, CreditCard, InvestmentAccount
from chittabook.models.categories import Category
from chittabook.models.transactions import Transaction
from django.utils.html import format_html
from django.utils import timezone


# create userprofile model form
class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'dob', 'profession', 'gender', 'country']
        widgets = {
            'dob': TextInput(     
        attrs={'type': 'date'} 
    ),
            'country': CountrySelectWidget()
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
        fields = '__all__'
        exclude = ['user']



# Credit Cards form
class CreditCardForm(ModelForm):
    class Meta:
        model = CreditCard
        fields = '__all__'
        exclude = ['user', 'debt']
        labels = {
            'balance': 'Initial Debt',
            'account_name': 'Credit Card Name',
        }



# Loan Account form
class LoanAccountForm(ModelForm):
    class Meta:
        model = LoanAccount
        fields = '__all__'
        exclude = ['user']



# Investment Account form
class InvestmentAccountForm(ModelForm):
    class Meta:
        model = InvestmentAccount
        fields = '__all__'
        exclude = ['user']


# Transaction form
class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        exclude = ['user', 'balance_after', 'created_at']
        widgets = {
            'date': TextInput(     
        attrs={'type': 'date'} 
    ),
        }

        
        
        