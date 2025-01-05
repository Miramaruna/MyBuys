from django.urls import path
from apps.main.views import home

urlpatterns = [
    path('', home, name="home")
]