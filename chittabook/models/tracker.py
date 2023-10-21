from django.db import models
from .usermodel import User
from .userprofile import UserProfile


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.subcategory_name

class Income(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    person_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    description = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Income: {self.amount}"

class Expense(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    person_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    description = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Expense: {self.amount}"

class Budget(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Budget: {self.amount}"