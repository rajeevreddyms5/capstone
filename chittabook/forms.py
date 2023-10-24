from django.forms import ModelForm, widgets, ValidationError
# import userprofile model from chittabook/models/userprofile.py
from chittabook.models.userprofile import UserProfile
from django_countries.widgets import CountrySelectWidget
from bootstrap_datepicker_plus.widgets import DatePickerInput
from datetime import date
from chittabook.models.accounts import BankAccount, LoanAccount, CreditCards, InvestmentAccount

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