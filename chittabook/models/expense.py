from django.db import models
from .usermodel import User
from .accounts import BankAccount, LoanAccount, CreditCards, InvestmentAccount
from django.utils.timezone import localtime

# expense category
class ExpenseCategory(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=256)
	created_at = models.DateTimeField(default=localtime)

	def __str__(self):
		return str(self.user) + self.name

	class Meta:
		verbose_name_plural = 'Expense Categories'


# expense
class Expense(models.Model):
	# choices
	BankAccounts = BankAccount.objects.all()
	LoanAccounts = LoanAccount.objects.all()
	CreditCards = CreditCards.objects.all()
	InvestmentAccount = InvestmentAccount.objects.all()

	# account_choices from BankAccount, LoanAccount, CreditCards, InvestmentAccount
	ACCOUNT_CHOICES = [
		('BankAccounts', 'Bank Accounts'),
		('LoanAccounts', 'Loan Accounts'),
		('CreditCards', 'Credit Cards'),
		('InvestmentAccounts', 'Investment Accounts'),
	]

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	account = models.CharField(max_length=256, choices=ACCOUNT_CHOICES)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	date = models.DateField(default=localtime)
	description = models.TextField()
	category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
	created_at = models.DateTimeField(default=localtime)

	def __str__(self):
		return str(self.category) + str(self.date) + str(self.amount)

	class Meta:
		ordering = ['-date']



