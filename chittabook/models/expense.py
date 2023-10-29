from django.db import models
from .usermodel import User
from .accounts import BankAccount, LoanAccount, CreditCards, InvestmentAccount
from django.utils.timezone import localtime

# expense category
class ExpenseCategory(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expensecategories')
	name = models.CharField(max_length=256)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Expense Categories'


# expense subcategory
class ExpenseSubCategory(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, related_name='expensesubcategories')
	name = models.CharField(max_length=256)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name_plural = 'Expense Subcategories'



# expense model
class Expense(models.Model):    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expensetransactions')
    account = models.CharField(max_length=256)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=localtime)
    note = models.CharField(max_length=256, blank=True, null=True)
    category = models.CharField(max_length=256)
    subcategory = models.CharField(max_length=256, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
 

    # override save method for updating balance on every save or deleting expense
    def save(self, *args, **kwargs):
        
       # self.user.bank_accounts.get(id=self.account).balance
        
        
        # Update the balance of the bank account
        self.account.balance -= self.amount
        self.account.save()

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Update the balance of the bank account
        self.account.balance += self.amount
        self.account.save()

        super().delete(*args, **kwargs)
            

    def __str__(self):
        return str(self.category) + str(self.date) + str(self.amount)

    class Meta:
        ordering = ['-date']



