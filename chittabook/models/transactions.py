from django.db import models
from .usermodel import User
from .category import Category


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    is_recurring = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"