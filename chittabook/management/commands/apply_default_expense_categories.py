from typing import Any
from django.core.management.base import BaseCommand
from chittabook.models.usermodel import User
from chittabook.models.expense import ExpenseCategory, ExpenseSubCategory
from chittabook.models.income import IncomeCategory, IncomeSubCategory
from django.apps import apps

class Command(BaseCommand):
    help = 'Apply default categories and subcategories to existing users (Both income and expense) - for expense "apply_default_expense_categories" and for income "apply_default_income_categories"'

    def handle(self, *args, **options):
        # Check if the apps are already loaded
        if apps.ready:
            self.apply_default_expense_categories()
        else:
            self.stdout.write("Apps are not ready yet. Retrying...")
            # Retry after a short delay
            import time
            time.sleep(1)
            self.handle(*args, **options)
    
    def apply_default_expense_categories(self):
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
            {'name': 'Travel', 'user': user},
            {'name': 'Vacation', 'user': user},
            {'name': 'Tax', 'user': user},
            {'name': 'Bank Charges', 'user': user},
            {'name': 'Childcare', 'user': user},
            {'name': 'Business', 'user': user},
            {'name': 'Miscellaneous', 'user': user},
        ]

            for category_data in categories:
                category, created = ExpenseCategory.objects.get_or_create(**category_data)
                if not created:
                    self.stdout.write(f"Category {category.name} already exists for user {user}. Skipping.")

            
            # create default subcategories
            subcategories = [
                {'category': ExpenseCategory.objects.get(name='ATM Withdrawals', user = user), 'name': 'Cash', 'user': user},
                {'category': ExpenseCategory.objects.get(name='ATM Withdrawals', user = user), 'name': 'Service Charge', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Automotive', user = user), 'name': 'Fuel', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Automotive', user = user), 'name': 'Service', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Bills', user = user), 'name': 'Electricity', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Bills', user = user), 'name': 'Water', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Bills', user = user), 'name': 'Internet', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Bills', user = user), 'name': 'Phone', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Bills', user = user), 'name': 'Gas', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Bills', user = user), 'name': 'Cable', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Bills', user = user), 'name': 'Rent', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Education', user = user), 'name': 'Fees', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Education', user = user), 'name': 'Books', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Entertainment', user = user), 'name': 'OTT Subscription', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Entertainment', user = user), 'name': 'Movies', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Entertainment', user = user), 'name': 'Sports', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Entertainment', user = user), 'name': 'Music', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Food', user = user), 'name': 'Restaurant', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Food', user = user), 'name': 'Snacks', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Food', user = user), 'name': 'Beverages', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Groceries', user = user), 'name': 'Fruits', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Groceries', user = user), 'name': 'Vegetables', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Healthcare', user = user), 'name': 'Medicines', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Healthcare', user = user), 'name': 'Pharmacy', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Healthcare', user = user), 'name': 'Hospital', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Home', user = user), 'name': 'Maintenance', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Home', user = user), 'name': 'Furnishing', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Home', user = user), 'name': 'Misc', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Insurance', user = user), 'name': 'Health Insurance', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Insurance', user = user), 'name': 'Life Insurance', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Investments', user = user), 'name': 'Mutual Funds', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Investments', user = user), 'name': 'Stocks', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Loan', user = user), 'name': 'Personal Loan', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Loan', user = user), 'name': 'Home Loan', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Loan', user = user), 'name': 'Car Loan', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Loan', user = user), 'name': 'Education Loan', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Personal', user = user), 'name': 'Clothing', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Personal', user = user), 'name': 'Personal Care', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Travel', user = user), 'name': 'Transport', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Travel', user = user), 'name': 'Hotel', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Travel', user = user), 'name': 'Taxi', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Vacation', user = user), 'name': 'Hotel', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Vacation', user = user), 'name': 'Transport', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Vacation', user = user), 'name': 'Taxi', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Vacation', user = user), 'name': 'Misc', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Tax', user = user), 'name': 'Income Tax', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Tax', user = user), 'name': 'Property Tax', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Childcare', user = user), 'name': 'Diapers', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Business', user = user), 'name': 'Reimbursed Expenses', 'user': user},
                {'category': ExpenseCategory.objects.get(name='Business', user = user), 'name': 'Non Reimbursed Expenses', 'user': user},
                
                # add more subcategories here
            ]

            for subcategory_data in subcategories:
                subcategory, created = ExpenseSubCategory.objects.get_or_create(**subcategory_data)
                if not created:
                    self.stdout.write(f"Subcategory {subcategory.name} already exists for user {user}. Skipping.")