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

        # custom validation for dob
        def clean_dob(self):
            dob = self.cleaned_data['dob']
            if dob > date.today():
                raise forms.ValidationError("Date of birth cannot be in the future")
            elif dob < date(1900, 1, 1):
                raise forms.ValidationError("Date of birth cannot be before 1900")
            elif dob and dob > date.today() + relativedelta(years=-13):
                raise forms.ValidationError("You must be at least 13 years old")
            return dob
        