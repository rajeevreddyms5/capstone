from django.db import models
from .usermodel import User


# class category model
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    category_type = models.CharField(max_length=30, choices=[('expense', 'Expense'), ('income', 'Income')], default='expense')
    category = models.CharField(max_length=30)
    sub_category = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.sub_category:
            return f"{self.category}:{self.sub_category}"
        else:
            return self.category

    class Meta:
        verbose_name_plural = 'Categories'
        unique_together = ('user', 'category', 'sub_category')
        ordering = ['category', 'sub_category']
        