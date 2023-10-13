from django.db import models
from django.forms import ModelForm
from .usermodel import User
from django_countries.fields import CountryField


# UserProfile
class UserProfile(models.Model):
    # choices
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    gender_choice = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Prefer not to say'),
    ]
    
    PROFESSION_CHOICES =[
        ("Employee","Employee"),
        ("Business","Business"),
        ("Student","Student"),
        ("Other","Other")
    ]

    # fields
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    profession = models.CharField(max_length=255, null=True, blank=True, choices=PROFESSION_CHOICES)
    gender = models.CharField(max_length=255, null=True, blank=True, choices=gender_choice)
    country = CountryField()
    numeric = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.name
    
    
    
# create userprofile model form
class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'dob', 'profession', 'gender', 'country', 'numeric']

    # override save method to update user profile instead of creating a new one
    def save(self, commit=True):
        user_profile = super(UserProfileForm, self).save(commit=False)
        user_profile.user = self.instance.user
        if commit:
            user_profile.save()
        return user_profile
