from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile, User
from chittabook.models.expense import ExpenseSubCategory, ExpenseCategory

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


@receiver(post_save, sender=User)
def create_default_categories(sender, instance, created, **kwargs):
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
            {'name': 'Shopping', 'user': instance},
            {'name': 'Travel', 'user': instance},
            {'name': 'Vacation', 'user': instance},
            {'name': 'Tax', 'user': instance},
            {'name': 'Bank Charges', 'user': instance},
            {'name': 'Childcare', 'user': instance},
            {'name': 'Business', 'user': instance},
            {'name': 'Miscellaneous', 'user': instance},
        ]

        for category_data in categories:
            ExpenseCategory.objects.create(user=instance, **category_data)

        
        # create default subcategories
        subcategories = [
            {'category': 'ATM Withdrawals', 'name': '[Cash, Service Charge]', 'user': instance},
            # add more subcategories here
        ]

        for subcategory_data in subcategories:
            ExpenseSubCategory.objects.create(user=instance, **subcategory_data)