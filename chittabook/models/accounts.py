from django.db import models
from .usermodel import User


class SavingsAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Bank Account - {self.account_name}"
    

class CheckingAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.account_name
    


class LoanAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lender = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Loan - {self.lender}"


class CreditCardAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_name = models.CharField(max_length=100)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Credit Card - {self.card_number}"


class InvestmentAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=100)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    current_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Investment Account - {self.account_number}"