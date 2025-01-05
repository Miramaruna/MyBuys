from django.shortcuts import render, redirect

# models
from apps.main.models import Item

# Create your views here.

def home(request):
    if request.method == 'POST':
        item_name = request.POST.get('item')
        if item_name:
            Item.objects.create(name=item_name)
        return redirect('home')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return redirect('home')
