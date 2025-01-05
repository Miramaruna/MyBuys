from django.shortcuts import render

# models
from apps.main.models import Item

# Create your views here.

def home(request):
    home = Item.objects.all()
    return render(request, home, locals())