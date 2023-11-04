from django.db import models
from .usermodel import User


# Base Accounts Model
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.account_name


class BankAccount(Account):
    pass


class LoanAccount(Account):
    principal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


class CreditCard(Account):
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2)
    initial_debt = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        if not self.pk:  # check if it's the first save
            self.balance = self.credit_limit - self.initial_debt
        super().save(*args, **kwargs)


class InvestmentAccount(Account):
    pass


# Update related_name based on account type
BankAccount.user.related_name = 'bank_accounts'
LoanAccount.user.related_name = 'loan_accounts'
CreditCard.user.related_name = 'credit_cards'
InvestmentAccount.user.related_name = 'investment_accounts'

# update verbose name based on account type for account_name field
BankAccount.account_name.verbose_name = 'Bank Account'
LoanAccount.account_name.verbose_name = 'Loan Account'
CreditCard.account_name.verbose_name = 'Credit Card'
InvestmentAccount.account_name.verbose_name = 'Investment Account'
