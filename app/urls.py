from django.urls import path
from .views import index, consContato
urlpatterns = [
    path('', index, name = 'index'),
    path('consContato/<int:pk>', consContato, name="consContato"),
]