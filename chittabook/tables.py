from .models import UserProfile, User, BankAccount, LoanAccount, CreditCards, InvestmentAccount, Expense, Income, ExpenseCategory, ExpenseSubCategory, IncomeCategory, IncomeSubCategory
import django_tables2 as tables
import itertools


# Expense table
class ExpenseTable(tables.Table):
    class Meta:
        model = Expense
        sequence = ('date', 'account', 'category', 'subcategory', 'amount')
        exclude = ('id', 'user', 'note', 'created_at')
        template_name = 'django_tables2/bootstrap5-responsive.html'
    
    # add serial number to the table
    def render_row_number(self):
        self.row.number = getattr(self, 'number', itertools.count())
        return next(self.row.number)