from django.db import models
from .usermodel import User
from .accounts import BankAccount, LoanAccount, CreditCards, InvestmentAccount
from django.utils.timezone import localtime

# expense category
class ExpenseCategory(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=256)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.user) + self.name

	class Meta:
		verbose_name_plural = 'Expense Categories'


# expense subcategory
class ExpenseSubCategory(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, related_name='subcategories')
	name = models.CharField(max_length=256)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.category) + self.name
	
	class Meta:
		verbose_name_plural = 'Expense Subcategories'


# expense
class Expense(models.Model):	
	
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	account = models.CharField(max_length=256)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	date = models.DateField(default=localtime)
	note = models.CharField(max_length=256, blank=True, null=True)
	category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.category) + str(self.date) + str(self.amount)

	class Meta:
		ordering = ['-date']



