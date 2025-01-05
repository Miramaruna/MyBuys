from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название категории"
        )

class Item(models.Model):
    category = models.ManyToManyField(Category, related_name="items")
    
    name = models.CharField(
        max_length=100,
        verbose_name="Название продукта"
        )