from typing import Any
from django.core.management.base import BaseCommand
from chittabook.models.usermodel import User
from capstone.chittabook.models.transactions import ExpenseCategory, ExpenseSubCategory
from capstone.chittabook.models.categories import IncomeCategory, IncomeSubCategory
from django.apps import apps

class Command(BaseCommand):
    help = 'Apply default categories and subcategories to existing users (Both income and expense) - for expense "apply_default_expense_categories" and for income "apply_default_income_categories"'

    def handle(self, *args, **options):
        # Check if the apps are already loaded
        if apps.ready:
            self.apply_default_income_categories()
        else:
            self.stdout.write("Apps are not ready yet. Retrying...")
            # Retry after a short delay
            import time
            time.sleep(1)
            self.handle(*args, **options)
    

    # apply default categories for income
    def apply_default_income_categories(self):
        users = User.objects.all()
        for user in users:
            categories = [
            {'name': 'Initial Balance', 'user': user},
            {'name': 'Salary', 'user': user},
            {'name': 'Retirement Income', 'user': user},
            {'name': 'Other Income', 'user': user},
            {'name': 'Investment Income', 'user': user},
        ]

            for category_data in categories:
                category, created = IncomeCategory.objects.get_or_create(**category_data)
                if not created:
                    self.stdout.write(f"Category {category.name} already exists for user {user}. Skipping.")

            
            # create default subcategories
            subcategories = [
                {'category': IncomeCategory.objects.get(name='Investment Income', user = user), 'name': 'Dividends', 'user': user},
                {'category': IncomeCategory.objects.get(name='Investment Income', user = user), 'name': 'Interest', 'user': user},
                {'category': IncomeCategory.objects.get(name='Investment Income', user = user), 'name': 'Long-term Capital Gains', 'user': user},
                {'category': IncomeCategory.objects.get(name='Investment Income', user = user), 'name': 'Short-term Capital Gains', 'user': user},
                {'category': IncomeCategory.objects.get(name='Other Income', user = user), 'name': 'Gifts Received', 'user': user},
                {'category': IncomeCategory.objects.get(name='Other Income', user = user), 'name': 'Loan Principal Received', 'user': user},
                {'category': IncomeCategory.objects.get(name='Other Income', user = user), 'name': 'Lotteries', 'user': user},
                {'category': IncomeCategory.objects.get(name='Retirement Income', user = user), 'name': 'Pensions/Annuities', 'user': user},
                {'category': IncomeCategory.objects.get(name='Retirement Income', user = user), 'name': 'Social Security', 'user': user},
                {'category': IncomeCategory.objects.get(name='Salary', user = user), 'name': 'Bonus', 'user': user},
                {'category': IncomeCategory.objects.get(name='Salary', user = user), 'name': 'Commission', 'user': user},
                {'category': IncomeCategory.objects.get(name='Salary', user = user), 'name': 'Overtime', 'user': user},
                {'category': IncomeCategory.objects.get(name='Salary', user = user), 'name': 'Employer Matching', 'user': user},
                {'category': IncomeCategory.objects.get(name='Salary', user = user), 'name': 'Paycheck', 'user': user},
                {'category': IncomeCategory.objects.get(name='Salary', user = user), 'name': 'Travel Allowance', 'user': user},

                # add more subcategories here
            ]

            for subcategory_data in subcategories:
                subcategory, created = IncomeSubCategory.objects.get_or_create(**subcategory_data)
                if not created:
                    self.stdout.write(f"Subcategory {subcategory.name} already exists for user {user}. Skipping.")