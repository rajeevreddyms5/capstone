from django.forms import ModelForm, widgets, ValidationError
# import userprofile model from chittabook/models/userprofile.py
from chittabook.models.userprofile import UserProfile
from django_countries.widgets import CountrySelectWidget
from bootstrap_datepicker_plus.widgets import DatePickerInput
from datetime import date

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
        elif dob > date.today() - date(100, 0, 0):
            raise ValidationError("Date of Birth cannot be more than 100 years.")
        # dob cannot be less than 13 years old
        elif dob < date.today() - date(13, 0, 0):
            raise ValidationError("Date of Birth cannot be less than 13 years.")
        
        return cleaned_data
            