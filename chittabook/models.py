from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from .utils import load_currency_data
from django_countries import CountryField
from djmoney.models.fields import CurrencyField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _


# define custom usermanger with email authentication
class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, **extra_fields)
    return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)


# define currency choices
CURRENCY_CHOICES = (
    ('USD', _('US Dollar')),
    ('EUR', _('Euro')),
    # Add more currency choices here
)


# CountryCurrencyField
class CountryCurrencyField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 2
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs.pop('max_length', None)
        return name, path, args, kwargs

@receiver(pre_save)
def update_currency(sender, instance, **kwargs):
    if isinstance(instance, UserProfile):
        if instance.country:
            instance.currency = instance.country.currency 

# UserProfile
class UserProfile(models.Model):
    # choices
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    gender_choice = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'prefer not to say'),
    ]

    # fields
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True, choices=gender_choice)
    country = CountryField()
    currency = CurrencyField(choices=CURRENCY_CHOICES, default='INR')
    numeric = models.CharField(max_length=255, null=True, blank=True)

    # save methods
    def save(self, *args, **kwargs):
       if self.country:
           self.currency = self.country.currency
       super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

