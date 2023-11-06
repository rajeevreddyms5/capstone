from django.db import models
from .usermodel import User
from django.db.utils import IntegrityError


# modify field values for subclass models
def modify_fields(**kwargs):
        def wrap(cls):
            for field, prop_dict in kwargs.items():
                for prop, val in prop_dict.items():
                    setattr(cls._meta.get_field(field), prop, val)
            return cls
        return wrap


# Base Accounts Model
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    # return account name 
    def __str__(self):
        return self.account_name
    

# Bank Account model
class BankAccount(Account):
    pass


# Credit Cards Model
class CreditCard(Account):
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Credit Card Debt')

    # on first save, based on credit limit and initial debt balance available will be updated
    def save(self, *args, **kwargs):
        if not self.pk:  # check if it's the first save
            if not self.credit_limit:
                self.debt = 0
            else:
                self.debt = self.credit_limit - self.balance
        super().save(*args, **kwargs)


# Loan Account Model
class LoanAccount(Account):
    principal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


# Investment Account model
class InvestmentAccount(Account):
    pass


