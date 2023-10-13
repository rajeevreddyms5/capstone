from django.forms import ModelForm, widgets
from django import forms
# import userprofile model from chittabook/models/userprofile.py
from chittabook.models.userprofile import UserProfile
from django_countries.widgets import CountrySelectWidget
from bootstrap_datepicker_plus.widgets import DatePickerInput

# Create your custom views here.


# create userprofile model form
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'dob', 'profession', 'gender', 'country']
        widgets = {
            'dob': DatePickerInput(),
            'country': CountrySelectWidget(),
        }