from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название категории"
        )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Item(models.Model):
    category = models.ManyToManyField(Category, related_name="items")
    
    name = models.CharField(
        max_length=100,
        verbose_name="Название продукта"
        )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"