from django.db import models
from .usermodel import User
from datetime import date, datetime, time
from babel.dates import format_date, format_datetime, format_time
import pycountry


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
    name = models.CharField(max_length=255)
    dob = models.DateField()
    profession = models.CharField(max_length=255, null=True, blank=True, choices=PROFESSION_CHOICES)
    gender = models.CharField(max_length=255, null=True, blank=True, choices=gender_choice)

    


    def __str__(self):
        return self.name
    
    
    

