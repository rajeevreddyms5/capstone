from django.db import models
from .usermodel import User
from .accounts import BankAccount, LoanAccount, CreditCards, SavingsAccount
from django.utils.timezone import localtime

# expense category
class ExpenseCategory(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length = 256)
	created_at = models.DateTimeField(default=localtime)

	def __str__(self):
		return str(self.user) + self.name

	class Meta:
		verbose_name_plural = 'Expense Categories'


# expense
class Expense(models.Model):
	
    # account_choices from BankAccount, LoanAccount, CreditCards, SavingsAccount
    account_choices_list = (
		BankAccount.objects.all(),
        LoanAccount.objects.all(),
        CreditCards.objects.all(),
        SavingsAccount.objects.all(),
    )
	
    user = models.ForeignKey(User, on_delete=models.CASCADE)
	account = models.ForeignKey(choices=account_choices_list, on_delete=models.CASCADE)
	amount = models.FloatField()
	date = models.DateField(default = localtime)
	description = models.TextField()
	category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
	created_at = models.DateTimeField(default=localtime)

	def __str__(self):
		return str(self.category) + str(self.date )+ str(self.amount)

	class Meta:
		ordering:['-date']



