from allauth.account.models import EmailAddress
from allauth.account.utils import perform_login
from django.forms import ValidationError
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from .models import User
from disposable_email_domains import blocklist

class SocialAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        """
        Invoked just after a user successfully authenticates via a
        social provider, but before the login is actually processed
        (and before the pre_social_login signal is emitted).

        We're trying to solve different use cases:
        - social account already exists, just go on
        - social account has no email or email is unknown, just go on
        - social account's email exists, link social account to existing user
        """

        # Ignore existing social accounts, just do this stuff for new ones
        if sociallogin.is_existing:
            return

        # some social logins don't have an email address, e.g. facebook accounts
        # with mobile numbers only, but allauth takes care of this case so just
        # ignore it
        if 'email' not in sociallogin.account.extra_data:
            return

        # check if given email address already exists.
        # Note: __iexact is used to ignore cases
        try:
            email = sociallogin.account.extra_data['email'].lower()
            email_address = EmailAddress.objects.get(email__iexact=email)

        # if it does not, let allauth take care of this new social account
        except EmailAddress.DoesNotExist:
            return

        # if it does, connect this new social login to the existing user
        user = email_address.user
        sociallogin.connect(request, user)


# email address validation
class RestrictEmailAdapter(DefaultAccountAdapter):
    # restrict email address registration from disposable emails
    def clean_email(self, email):
        domain = email.lower().split('@')[1]

        # if email is already registered and not verified
        if EmailAddress.objects.filter(email=email, verified=False).exists():
            raise ValidationError('You are already registered with this email. Please verify your email.')
        
        # if email is already registered and verified
        if EmailAddress.objects.filter(email=email, verified=True).exists():
            raise ValidationError('You are already registered with this email. Please login.')
        
        # if email is from any blocklisted domain prevent from signing up        
        if domain in blocklist:
            raise ValidationError('You are restricted from registering with this email. Please contact admin.')
        
        # you can block any email from registering in your website
        if email in ['']:
            raise ValidationError('You are restricted from registering with this email. Please contact admin.')
        return email
        