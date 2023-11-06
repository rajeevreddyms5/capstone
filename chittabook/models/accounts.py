from typing import Any
from django.db import models
from .usermodel import User
from django.db.utils import IntegrityError


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
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    # override save method to set balance to negative value if balance entered by user is positive
    def save(self, *args, **kwargs):
        if self.balance > 0:
            self.balance = -self.balance
        super().save(*args, **kwargs)
    
        

# Loan Account Model
class LoanAccount(Account):
    principal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    # override save method to set balance to negative value if balance entered by user is positive
    def save(self, *args, **kwargs):
        if self.balance > 0:
            self.balance = -self.balance
        super().save(*args, **kwargs)


# Investment Account model
class InvestmentAccount(Account):
    pass


