from .models import UserProfile, User, BankAccount, LoanAccount, CreditCards, InvestmentAccount, Expense, Income, ExpenseCategory, ExpenseSubCategory, IncomeCategory, IncomeSubCategory
import django_tables2 as tables


# Expense table
class ExpenseTable(tables.Table):
    class Meta:
        model = Expense