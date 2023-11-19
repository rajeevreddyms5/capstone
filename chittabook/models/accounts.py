from typing import Any
from django.db import models
from .usermodel import User
from .userprofile import UserProfile
from django.db.utils import IntegrityError
from django.utils.timezone import localtime

# Base Accounts Model
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
                
    # return account name 
    def __str__(self):
        return self.account_name
    
    '''
     # override save method to set initial balance as transaction for initial balance
    def save(self, *args, **kwargs):
        if not self.pk:  # Only for new instances
            from .transactions import Transaction  # Import here to avoid circular import
            from .categories import Category
            transaction = Transaction.objects.create(user=self.user, account=self, amount=self.balance, category=Category.objects.get(user=self.user, category='Initial Balance', category_type='income'), description='Initial Balance')
            transaction.save()
        super().save(*args, **kwargs)
    '''
   
    

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


