from decimal import Decimal
from django.db.models import Q
import django_filters
from .models import User, UserProfile, Account, BankAccount, LoanAccount, CreditCard, InvestmentAccount, Category, Transaction


# create transaction filter
class TransactionFilter(django_filters.FilterSet):

    query = django_filters.CharFilter(
        method='universal_search',
        label='Search',
    )

    class Meta:
        model = Transaction
        fields = ['query']

    def universal_search(self, queryset, name, value):
        if value.replace(".", "", 1).isdigit():
            value = Decimal(value)
            return Transaction.objects.filter(
                Q(amount=value) | Q(date=value)
            )

        return Transaction.objects.filter(
            Q(account__icontains=value) | Q(category__icontains=value)
        )