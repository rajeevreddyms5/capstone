from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . models import User, UserProfile, Account, BankAccount, LoanAccount, CreditCard, InvestmentAccount, Category, Transaction

# Register your models here.
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active', 
            'is_staff', 
            'is_superuser',
            'groups', 
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'name', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

# register userprofile model
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Account)
admin.site.register(BankAccount)
admin.site.register(LoanAccount)
admin.site.register(CreditCard)
admin.site.register(InvestmentAccount)
admin.site.register(Transaction)
admin.site.register(User, UserAdmin)