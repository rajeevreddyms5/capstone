from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile, User
from .models import Account, BankAccount, LoanAccount, CreditCard, InvestmentAccount, Category, Transaction


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
def create_default_categories(sender, instance, created, **kwargs):
    if created:
        # create default categories
        categories = [
            # expense categories
            {'category_type': 'expense', 'category': 'ATM Withdrawals', 'sub_category': None, 'user': instance},
            {'category_type': 'expense', 'category': 'Automotive', 'sub_category': None, 'user': instance},
            {'category_type': 'expense', 'category': 'Bills', 'sub_category': None, 'user': instance},
            {'category_type': 'expense', 'category': 'Education', 'sub_category': None, 'user': instance},
            {'category_type': 'expense', 'category': 'Entertainment', 'sub_category': None, 'user': instance},
            {'category_type': 'expense', 'category': 'Food', 'sub_category': None, 'user': instance},
            {'category_type': 'expense', 'category': 'Gifts', 'sub_category': None, 'user': instance},
            {'category_type': 'expense', 'category': 'Groceries', 'sub_category': None, 'user': instance},
            {'category_type': 'expense', 'category': 'Healthcare', 'sub_category': None, 'user': instance},
            {'category_type': 'expense', 'category': 'Home', 'sub_category': None, 'user': instance},
            {'category_type': 'expense', 'category': 'Insurance', 'sub_category': None, 'user': instance},
            {'category_type': 'expense', 'category': 'Investments', 'sub_category': None, 'user': instance},
            {'category_type': 'expense', 'category': 'Loan', 'sub_category': None, 'user': instance},
            {'category_type': 'expense', 'category': 'Personal', 'sub_category': None, 'user': instance},
            {'category_type': 'expense', 'category': 'Travel', 'sub_category': None, 'user': instance},
            {'category_type': 'expense', 'category': 'Vacation', 'sub_category': None, 'user': instance},
            {'category_type': 'expense', 'category': 'Tax', 'sub_category': None, 'user': instance},
            {'category_type': 'expense', 'category': 'Bank Charges', 'sub_category': None, 'user': instance},
            {'category_type': 'expense', 'category': 'Childcare', 'sub_category': None, 'user': instance},
            {'category_type': 'expense', 'category': 'Business', 'sub_category': None, 'user': instance},
            {'category_type': 'expense', 'category': 'Miscellaneous', 'sub_category': None, 'user': instance},
            
            {'category_type': 'expense', 'category': 'ATM Withdrawals', 'sub_category': 'Cash', 'user': instance},
            {'category_type': 'expense', 'category': 'ATM Withdrawals', 'sub_category': 'Service Charge', 'user': instance},
            {'category_type': 'expense', 'category': 'Automotive', 'sub_category': 'Fuel', 'user': instance},
            {'category_type': 'expense', 'category': 'Automotive', 'sub_category': 'Service', 'user': instance},
            {'category_type': 'expense', 'category': 'Bills', 'sub_category': 'Electricity', 'user': instance},
            {'category_type': 'expense', 'category': 'Bills', 'sub_category': 'Water', 'user': instance},
            {'category_type': 'expense', 'category': 'Bills', 'sub_category': 'Internet', 'user': instance},
            {'category_type': 'expense', 'category': 'Bills', 'sub_category': 'Phone', 'user': instance},
            {'category_type': 'expense', 'category': 'Bills', 'sub_category': 'Gas', 'user': instance},
            {'category_type': 'expense', 'category': 'Bills', 'sub_category': 'Cable', 'user': instance},
            {'category_type': 'expense', 'category': 'Bills', 'sub_category': 'Rent', 'user': instance},
            {'category_type': 'expense', 'category': 'Education', 'sub_category': 'Fees', 'user': instance},
            {'category_type': 'expense', 'category': 'Education', 'sub_category': 'Books', 'user': instance},
            {'category_type': 'expense', 'category': 'Entertainment', 'sub_category': 'OTT Subscription', 'user': instance},
            {'category_type': 'expense', 'category': 'Entertainment', 'sub_category': 'Movies', 'user': instance},
            {'category_type': 'expense', 'category': 'Entertainment', 'sub_category': 'Sports', 'user': instance},
            {'category_type': 'expense', 'category': 'Entertainment', 'sub_category': 'Music', 'user': instance},
            {'category_type': 'expense', 'category': 'Food', 'sub_category': 'Restaurant', 'user': instance},
            {'category_type': 'expense', 'category': 'Food', 'sub_category': 'Snacks', 'user': instance},
            {'category_type': 'expense', 'category': 'Food', 'sub_category': 'Beverages', 'user': instance},
            {'category_type': 'expense', 'category': 'Groceries', 'sub_category': 'Fruits', 'user': instance},
            {'category_type': 'expense', 'category': 'Groceries', 'sub_category': 'Vegetables', 'user': instance},
            {'category_type': 'expense', 'category': 'Healthcare', 'sub_category': 'Medicines', 'user': instance},
            {'category_type': 'expense', 'category': 'Healthcare', 'sub_category': 'Pharmacy', 'user': instance},
            {'category_type': 'expense', 'category': 'Healthcare', 'sub_category': 'Hospital', 'user': instance},
            {'category_type': 'expense', 'category': 'Home', 'sub_category': 'Maintenance', 'user': instance},
            {'category_type': 'expense', 'category': 'Home', 'sub_category': 'Furnishing', 'user': instance},
            {'category_type': 'expense', 'category': 'Home', 'sub_category': 'Misc', 'user': instance},
            {'category_type': 'expense', 'category': 'Insurance', 'sub_category': 'Life Insurance', 'user': instance},
            {'category_type': 'expense', 'category': 'Insurance', 'sub_category': 'Health Insurance', 'user': instance},
            {'category_type': 'expense', 'category': 'Insurance', 'sub_category': 'Car Insurance', 'user': instance},
            {'category_type': 'expense', 'category': 'Investments', 'sub_category': 'Mutual Funds', 'user': instance},
            {'category_type': 'expense', 'category': 'Investments', 'sub_category': 'Stocks', 'user': instance},
            {'category_type': 'expense', 'category': 'Loan', 'sub_category': 'Personal Loan', 'user': instance},
            {'category_type': 'expense', 'category': 'Loan', 'sub_category': 'Home Loan', 'user': instance},
            {'category_type': 'expense', 'category': 'Loan', 'sub_category': 'Car Loan', 'user': instance},
            {'category_type': 'expense', 'category': 'Loan', 'sub_category': 'Education Loan', 'user': instance},
            {'category_type': 'expense', 'category': 'Personal', 'sub_category': 'Clothing', 'user': instance},
            {'category_type': 'expense', 'category': 'Personal', 'sub_category': 'Personal Care', 'user': instance},
            {'category_type': 'expense', 'category': 'Travel', 'sub_category': 'Transport', 'user': instance},
            {'category_type': 'expense', 'category': 'Travel', 'sub_category': 'Hotel', 'user': instance},
            {'category_type': 'expense', 'category': 'Travel', 'sub_category': 'Taxi', 'user': instance},
            {'category_type': 'expense', 'category': 'Vacation', 'sub_category': 'Misc', 'user': instance},
            {'category_type': 'expense', 'category': 'Tax', 'sub_category': 'Income Tax', 'user': instance},
            {'category_type': 'expense', 'category': 'Tax', 'sub_category': 'Property Tax', 'user': instance},
            {'category_type': 'expense', 'category': 'Tax', 'sub_category': 'Water Tax', 'user': instance},
            {'category_type': 'expense', 'category': 'Childcare', 'sub_category': 'Diapers', 'user': instance},
            {'category_type': 'expense', 'category': 'Business', 'sub_category': 'Reimbursed expenses', 'user': instance},
            {'category_type': 'expense', 'category': 'Business', 'sub_category': 'Non Reimbursed expenses', 'user': instance},
            
            # income categories
            {'category_type': 'income', 'category': 'Initial Balance', 'sub_category': None, 'user': instance},
            {'category_type': 'income', 'category': 'Salary', 'sub_category': None, 'user': instance},
            {'category_type': 'income', 'category': 'Retirement Income', 'sub_category': None, 'user': instance},
            {'category_type': 'income', 'category': 'Other Income', 'sub_category': None, 'user': instance},
            {'category_type': 'income', 'category': 'Investment Income', 'sub_category': None, 'user': instance},
            
            {'category_type': 'income', 'category': 'Investment Income', 'sub_category': 'Dividends', 'user': instance},
            {'category_type': 'income', 'category': 'Investment Income', 'sub_category': 'Interest', 'user': instance},
            {'category_type': 'income', 'category': 'Investment Income', 'sub_category': 'Long-term Capital Gains', 'user': instance},
            {'category_type': 'income', 'category': 'Investment Income', 'sub_category': 'Short-term Capital Gains', 'user': instance},
            {'category_type': 'income', 'category': 'Other Income', 'sub_category': 'Gifts Received', 'user': instance},
            {'category_type': 'income', 'category': 'Other Income', 'sub_category': 'Loan Principal Received', 'user': instance},
            {'category_type': 'income', 'category': 'Other Income', 'sub_category': 'Lotteries', 'user': instance},
            {'category_type': 'income', 'category': 'Retirement Income', 'sub_category': 'Pensions/Annuities', 'user': instance},
            {'category_type': 'income', 'category': 'Retirement Income', 'sub_category': 'Social Security', 'user': instance},
            {'category_type': 'income', 'category': 'Retirement Income', 'sub_category': 'Taxes', 'user': instance},
            {'category_type': 'income', 'category': 'Salary', 'sub_category': 'Bonus', 'user': instance},
            {'category_type': 'income', 'category': 'Salary', 'sub_category': 'Commission', 'user': instance},
            {'category_type': 'income', 'category': 'Salary', 'sub_category': 'Overtime', 'user': instance},
            {'category_type': 'income', 'category': 'Salary', 'sub_category': 'Employer Matching', 'user': instance},
            {'category_type': 'income', 'category': 'Salary', 'sub_category': 'Paycheck', 'user': instance},
            {'category_type': 'income', 'category': 'Salary', 'sub_category': 'Travel Allowance', 'user': instance},
        ]

        for category_data in categories:
            category, created = Category.objects.get_or_create(**category_data)
