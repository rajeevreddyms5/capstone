from .models import UserProfile, User, Account, BankAccount, LoanAccount, CreditCard, InvestmentAccount, Category, Transaction
import django_tables2 as tables


# Expense table
class TransactionTable(tables.Table):
    class Meta:
        model = Transaction
        sequence = ('date', 'account', 'category', 'amount')
        exclude = ('id', 'user', 'description', 'created_at', 'balance_after')
        template_name = 'tables/bootstrap_htmx.html'