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


# income model
class Income(models.Model):	
	
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incometransactions')
	account = models.CharField(max_length=256)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	date = models.DateField(default=localtime)
	note = models.CharField(max_length=256, blank=True, null=True)
	category = models.CharField(max_length=256)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.category) + str(self.date) + str(self.amount)

	class Meta:
		ordering = ['-date']
