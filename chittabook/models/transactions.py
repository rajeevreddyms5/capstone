from django.db import models
from .usermodel import User
from .accounts import Account, BankAccount, LoanAccount, CreditCard, InvestmentAccount
from .categories import Category
from django.utils.timezone import localtime



# Transactions model
class Transaction(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_transactions')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='account_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=localtime)
    description = models.CharField(max_length=256, blank=True, null=True, verbose_name='Note')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_transactions')
    balance_after = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
            

    def __str__(self):
        return str(self.category) + str(self.date) + str(self.amount)

    class Meta:
        ordering = ['-date']
