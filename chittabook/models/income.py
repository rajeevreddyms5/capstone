from django.db import models
from .usermodel import User
from .accounts import BankAccount, LoanAccount, CreditCards, InvestmentAccount
from django.utils.timezone import localtime

# income category
class IncomeCategory(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incomecategories')
	name = models.CharField(max_length=256)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Income Categories'


# income subcategory
class IncomeSubCategory(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE, related_name='incomesubcategories')
	name = models.CharField(max_length=256)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name_plural = 'Income Subcategories'


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incometransactions')
    account = models.CharField(max_length=256)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=localtime)
    note = models.CharField(max_length=256, blank=True, null=True)
    category = models.CharField(max_length=256)
    subcategory = models.CharField(max_length=256, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        try:
            # Update the balance of the bank account
            self.account.balance -= self.amount
            self.account.save()
        except AttributeError:
            income = Income.objects.get(id=self.id)
            account = income.account
            # split account name by '-' to get account type and account name
            account_type, account_name = self.account.split('-')
            if account_type == 'Bank Accounts':
                account = BankAccount.objects.get(id=account_name)
            elif account_type == 'Loan Accounts':
                account = LoanAccount.objects.get(id=account_name)
            elif account_type == 'Credit Cards':
                account = CreditCards.objects.get(id=account_name)
            elif account_type == 'Investment Accounts':
                account = CreditCards.objects.get(id=account_name)

            account.balance -= self.amount

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        try:
            # Update the balance of the bank account
            self.account.balance += self.amount
            self.account.save()
        except AttributeError:
            income = Income.objects.get(id=self.id)
            account = income.account
            # split account name by '-' to get account type and account name
            account_type, account_name = self.account.split('-')
            if account_type == 'Bank Accounts':
                account = BankAccount.objects.get(id=account_name)
                account.balance += self.amount
            elif account_type == 'Loan Accounts':
                account = LoanAccount.objects.get(id=account_name)
                account.balance += self.amount
            elif account_type == 'Credit Cards':
                account = CreditCards.objects.get(id=account_name)
                account.balance += self.amount
            elif account_type == 'Investment Accounts':
                account = CreditCards.objects.get(id=account_name)
                account.balance += self.amount

        super().delete(*args, **kwargs)

    def __str__(self):
        return str(self.category) + str(self.date) + str(self.amount)

    class Meta:
        ordering = ['-date']