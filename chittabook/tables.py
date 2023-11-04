from .models import UserProfile, User, Account, BankAccount, LoanAccount, CreditCard, InvestmentAccount, Category, Transaction
import django_tables2 as tables
import itertools


# Expense table
class TransactionTable(tables.Table):
    class Meta:
        model = Transaction
        sequence = ('date', 'account', 'category', 'sub_category', 'amount')
        exclude = ('id', 'user', 'description', 'created_at')
        template_name = 'django_tables2/bootstrap5-responsive.html'