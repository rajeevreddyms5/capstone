from django.forms import ModelForm, widgets
from django import forms
# import userprofile model from chittabook/models/userprofile.py
from chittabook.models.userprofile import UserProfile


# Create your custom views here.

# date picker for userprofile model form
class DateInput(forms.DateInput):
    input_type = 'date'

# create userprofile model form
class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'dob', 'profession', 'gender', 'country', 'numeric']
        widgets = {
            'order_date': widgets.DateInput(),
        }