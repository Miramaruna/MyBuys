from rest_framework import serializers

# models
from apps.main.models import Item

# ApiView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

# Views
from apps.main.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'category')

class ItemListApiView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
class ItemListCreateView(CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
class ItemListDeleteView(DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
class ItemListUpdateView(UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer