from typing import Any
from django.core.management.base import BaseCommand
from chittabook.models.usermodel import User
from chittabook.models.expense import ExpenseCategory, ExpenseSubCategory
from django.apps import chittabook

class Command(BaseCommand):
    help = 'Apply default categories and subcategories to existing users'

    def handle(self, *args, **options):
        # Check if the apps are already loaded
        if chittabook.ready:
            self.apply_default_categories()
        else:
            self.stdout.write("Apps are not ready yet. Retrying...")
            # Retry after a short delay
            import time
            time.sleep(1)
            self.handle(*args, **options)
    
    def apply_default_categories(self):
        users = User.objects.all()
        for user in users:
            categories = [
            {'name': 'ATM Withdrawals', 'user': user},
            {'name': 'Automotive', 'user': user},
            {'name': 'Bills', 'user': user},
            {'name': 'Education', 'user': user},
            {'name': 'Entertainment', 'user': user},
            {'name': 'Food', 'user': user},
            {'name': 'Gifts', 'user': user},
            {'name': 'Groceries', 'user': user},
            {'name': 'Healthcare', 'user': user},
            {'name': 'Home', 'user': user},
            {'name': 'Insurance', 'user': user},
            {'name': 'Investments', 'user': user},
            {'name': 'Loan', 'user': user},
            {'name': 'Personal', 'user': user},
            {'name': 'Shopping', 'user': user},
            {'name': 'Travel', 'user': user},
            {'name': 'Vacation', 'user': user},
            {'name': 'Tax', 'user': user},
            {'name': 'Bank Charges', 'user': user},
            {'name': 'Childcare', 'user': user},
            {'name': 'Business', 'user': user},
            {'name': 'Miscellaneous', 'user': user},
        ]

        for category_data in categories:
            ExpenseCategory.objects.create(user=user, **category_data)

        
        # create default subcategories
        subcategories = [
            {'category': 'ATM Withdrawals', 'name': '[Cash, Service Charge]', 'user': user},
            # add more subcategories here
        ]

        for subcategory_data in subcategories:
            ExpenseSubCategory.objects.create(user=user, **subcategory_data)