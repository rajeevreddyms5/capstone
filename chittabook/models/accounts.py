from django.db import models
from .usermodel import User


class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Bank Account - {self.account_name}"



class LoanAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lender_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Loan - {self.lender}"


class CreditCards(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_name = models.CharField(max_length=100)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2)
    initial_debt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    # update balance on first save from initial_debt to credit_limit not on every save
    def save(self, *args, **kwargs):
        if not self.pk:  # check if it's the first save
            self.balance = self.credit_limit - self.initial_debt
        super().save(*args, **kwargs)
        

    def __str__(self):
        return f"Credit Card - {self.card_number}"


class InvestmentAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=100)
    current_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Investment Account - {self.account_number}"