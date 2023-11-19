from .models import UserProfile, User, Account, BankAccount, LoanAccount, CreditCard, InvestmentAccount, Category, Transaction
import django_tables2 as tables
import itertools


# Expense table
class TransactionTable(tables.Table):

    T1     = '<a href="#" role="button" id={{ transaction.id }}><i class="bi bi-pencil-square" style="font-size: 20px;"></i></a>'
    T2     = '<a href="#" role="button" id={{ transaction.id }}><i class="bi bi-trash" style="font-size: 20px;"></i></a>'
    edit   = tables.TemplateColumn(T1)
    delete = tables.TemplateColumn(T2)
    
    # add formatter to display currency
    amount = tables.TemplateColumn('{% load babel %}{{ record.amount|currencyfmt:record.currency }}')



    class Meta:
        model = Transaction
        sequence = ('date', 'account', 'category', 'amount')
        exclude = ('id', 'user', 'description', 'created_at', 'balance_after', 'currency')
        template_name = 'tables/bootstrap_htmx.html'
        
        # id attribute for each row
        row_attrs = {
            "data-id": lambda record: record.pk
        }


