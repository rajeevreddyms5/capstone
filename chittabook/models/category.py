from django.db import models
from .usermodel import User


class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
