from django.db import models
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
    

