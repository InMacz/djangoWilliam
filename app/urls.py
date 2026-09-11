from django.urls import path
from .views import index, consContato, cadContato, altContato, delContato
urlpatterns = [
    path('', index, name = 'index'),
    path('consContato/<int:pk>', consContato, name="consContato"),
    path('cadContato', cadContato, name='cadContato'),
    path('altContato/<int:pk>', altContato, name="altContato"),
    path('delContato/<int:pk>', delContato, name="delContato"),
]