
# Create your custom view that inherits SignupView and overrides the form class
class CustomFormSignupView(allauth.accounts.views.SignupView):
    form_class = CustomSignupForm
    
# Create a custom form that inherits from SignupForm and overrides the email validation message
class CustomSignupForm(allauth.accounts.forms.SignupForm ):
    def raise_duplicate_email_error(self):
        # here I tried to override the method, but it is not called
        raise forms.ValidationError(
            _("An account already exists with this e-mail address."
              " Please sign in to that account."))