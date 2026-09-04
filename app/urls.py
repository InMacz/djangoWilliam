from django.urls import path
from .views import index, consContato, cadContato
urlpatterns = [
    path('', index, name = 'index'),
    path('consContato/<int:pk>', consContato, name="consContato"),
    path('cadContato', cadContato, name='cadContato'),
]