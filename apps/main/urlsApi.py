from django.urls import path

# Serializers
from apps.main.serializers import ItemListApiView, ItemListCreateView, ItemListDeleteView, ItemListUpdateView

urlpatterns = [
    path('', ItemListApiView.as_view(), name="ListApiView"),
    path('destroy/<int:pk>', ItemListDeleteView.as_view(), name="destroy"),
    path('update/<int:pk>', ItemListUpdateView.as_view(), name="update"),
    path('create/', ItemListCreateView.as_view(), name="create"),
]