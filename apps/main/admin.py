from django.contrib import admin
from .models import Item  # Импортируйте вашу модель Item

@admin.register(Item)  # Используйте декоратор правильно
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Уберите 'category' если это не поле модели Item
    search_fields = ('name',)
    # Уберите filter_horizontal, если у вас нет ManyToMany поля
    # filter_horizontal = ('category',)