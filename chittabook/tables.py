from .models import UserProfile, User, Account, BankAccount, LoanAccount, CreditCard, InvestmentAccount, Category, Transaction
import django_tables2 as tables
import itertools

# Expense table
class TransactionTable(tables.Table):

    T1     = '<button type="button" class="btn btn-outline-primary" id={{ transaction.id }}><i class="bi bi-pencil-square"></i></button>'
    T2     = '<button type="button" class="btn btn-outline-danger" id={{ transaction.id }}><i class="bi bi-trash"></i></button>'
    edit   = tables.TemplateColumn(T1)
    delete = tables.TemplateColumn(T2)
    
    # add formatter to display currency
    amount = tables.TemplateColumn('{{ record.amount|floatformat:2 }}')


    class Meta:
        model = Transaction
        sequence = ('date', 'account', 'category', 'amount')
        exclude = ('id', 'user', 'description', 'created_at', 'balance_after')
        template_name = 'tables/bootstrap_htmx.html'
        
        # id attribute for each row
        row_attrs = {
            "data-id": lambda record: record.pk
        }


