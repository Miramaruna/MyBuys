from django.urls import path

# Views
from apps.main.views import home, delete_item

urlpatterns = [
    path('', home, name="home"),
    path('delete/<int:item_id>/', delete_item, name='delete_item'),
]