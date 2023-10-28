from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile, User
from chittabook.models.expense import ExpenseSubCategory, ExpenseCategory
from chittabook.models.income import IncomeSubCategory, IncomeCategory


# create user profile when user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except:
        UserProfile.objects.create(user=instance)


# create default expense categories for each user when user is created
@receiver(post_save, sender=User)
def create_default_expense_categories(sender, instance, created, **kwargs):
    if created:
        # create default categories
        categories = [
            {'name': 'ATM Withdrawals', 'user': instance},
            {'name': 'Automotive', 'user': instance},
            {'name': 'Bills', 'user': instance},
            {'name': 'Education', 'user': instance},
            {'name': 'Entertainment', 'user': instance},
            {'name': 'Food', 'user': instance},
            {'name': 'Gifts', 'user': instance},
            {'name': 'Groceries', 'user': instance},
            {'name': 'Healthcare', 'user': instance},
            {'name': 'Home', 'user': instance},
            {'name': 'Insurance', 'user': instance},
            {'name': 'Investments', 'user': instance},
            {'name': 'Loan', 'user': instance},
            {'name': 'Personal', 'user': instance},
            {'name': 'Travel', 'user': instance},
            {'name': 'Vacation', 'user': instance},
            {'name': 'Tax', 'user': instance},
            {'name': 'Bank Charges', 'user': instance},
            {'name': 'Childcare', 'user': instance},
            {'name': 'Business', 'user': instance},
            {'name': 'Miscellaneous', 'user': instance},
        ]

        for category_data in categories:
            category, created = ExpenseCategory.objects.get_or_create(**category_data)

        
        # create default subcategories
        subcategories = [
                {'category': ExpenseCategory.objects.get(name='ATM Withdrawals', user = instance), 'name': 'Cash', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='ATM Withdrawals', user = instance), 'name': 'Service Charge', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Automotive', user = instance), 'name': 'Fuel', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Automotive', user = instance), 'name': 'Service', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Bills', user = instance), 'name': 'Electricity', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Bills', user = instance), 'name': 'Water', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Bills', user = instance), 'name': 'Internet', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Bills', user = instance), 'name': 'Phone', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Bills', user = instance), 'name': 'Gas', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Bills', user = instance), 'name': 'Cable', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Bills', user = instance), 'name': 'Rent', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Education', user = instance), 'name': 'Fees', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Education', user = instance), 'name': 'Books', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Entertainment', user = instance), 'name': 'OTT Subscription', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Entertainment', user = instance), 'name': 'Movies', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Entertainment', user = instance), 'name': 'Sports', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Entertainment', user = instance), 'name': 'Music', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Food', user = instance), 'name': 'Restaurant', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Food', user = instance), 'name': 'Snacks', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Food', user = instance), 'name': 'Beverages', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Groceries', user = instance), 'name': 'Fruits', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Groceries', user = instance), 'name': 'Vegetables', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Healthcare', user = instance), 'name': 'Medicines', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Healthcare', user = instance), 'name': 'Pharmacy', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Healthcare', user = instance), 'name': 'Hospital', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Home', user = instance), 'name': 'Maintenance', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Home', user = instance), 'name': 'Furnishing', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Home', user = instance), 'name': 'Misc', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Insurance', user = instance), 'name': 'Health Insurance', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Insurance', user = instance), 'name': 'Life Insurance', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Investments', user = instance), 'name': 'Mutual Funds', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Investments', user = instance), 'name': 'Stocks', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Loan', user = instance), 'name': 'Personal Loan', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Loan', user = instance), 'name': 'Home Loan', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Loan', user = instance), 'name': 'Car Loan', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Loan', user = instance), 'name': 'Education Loan', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Personal', user = instance), 'name': 'Clothing', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Personal', user = instance), 'name': 'Personal Care', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Travel', user = instance), 'name': 'Transport', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Travel', user = instance), 'name': 'Hotel', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Travel', user = instance), 'name': 'Taxi', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Vacation', user = instance), 'name': 'Hotel', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Vacation', user = instance), 'name': 'Transport', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Vacation', user = instance), 'name': 'Taxi', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Vacation', user = instance), 'name': 'Misc', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Tax', user = instance), 'name': 'Income Tax', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Tax', user = instance), 'name': 'Property Tax', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Childcare', user = instance), 'name': 'Diapers', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Business', user = instance), 'name': 'Reimbursed Expenses', 'user': instance},
                {'category': ExpenseCategory.objects.get(name='Business', user = instance), 'name': 'Non Reimbursed Expenses', 'user': instance},
                
                # add more subcategories here
            ]

        for subcategory_data in subcategories:
            subcategory, created = ExpenseSubCategory.objects.get_or_create(**subcategory_data)
    

# create default income categories for each user when user is created
@receiver(post_save, sender=User)
def create_default_income_categories(sender, instance, created, **kwargs):
    if created:
        # create default categories
        categories = [
            {'name': 'Initial Balance', 'user': instance},
            {'name': 'Salary', 'user': instance},
            {'name': 'Retirement Income', 'user': instance},
            {'name': 'Other Income', 'user': instance},
            {'name': 'Investment Income', 'user': instance},
           
        ]

        for category_data in categories:
            category, created = IncomeCategory.objects.get_or_create(**category_data)

        
        # create default subcategories
        subcategories = [
                {'category': IncomeCategory.objects.get(name='Investment Income', user = instance), 'name': 'Dividends', 'user': instance},
                {'category': IncomeCategory.objects.get(name='Investment Income', user = instance), 'name': 'Interest', 'user': instance},
                {'category': IncomeCategory.objects.get(name='Investment Income', user = instance), 'name': 'Long-term Capital Gains', 'user': instance},
                {'category': IncomeCategory.objects.get(name='Investment Income', user = instance), 'name': 'Short-term Capital Gains', 'user': instance},
                {'category': IncomeCategory.objects.get(name='Other Income', user = instance), 'name': 'Gifts Received', 'user': instance},
                {'category': IncomeCategory.objects.get(name='Other Income', user = instance), 'name': 'Loan Principal Received', 'user': instance},
                {'category': IncomeCategory.objects.get(name='Other Income', user = instance), 'name': 'Lotteries', 'user': instance},
                {'category': IncomeCategory.objects.get(name='Retirement Income', user = instance), 'name': 'Pensions/Annuities', 'user': instance},
                {'category': IncomeCategory.objects.get(name='Retirement Income', user = instance), 'name': 'Social Security', 'user': instance},
                {'category': IncomeCategory.objects.get(name='Salary', user = instance), 'name': 'Bonus', 'user': instance},
                {'category': IncomeCategory.objects.get(name='Salary', user = instance), 'name': 'Commission', 'user': instance},
                {'category': IncomeCategory.objects.get(name='Salary', user = instance), 'name': 'Overtime', 'user': instance},
                {'category': IncomeCategory.objects.get(name='Salary', user = instance), 'name': 'Employer Matching', 'user': instance},
                {'category': IncomeCategory.objects.get(name='Salary', user = instance), 'name': 'Paycheck', 'user': instance},
                {'category': IncomeCategory.objects.get(name='Salary', user = instance), 'name': 'Travel Allowance', 'user': instance},
            
                
                # add more subcategories here
            ]

        for subcategory_data in subcategories:
            subcategory, created = IncomeSubCategory.objects.get_or_create(**subcategory_data)
              