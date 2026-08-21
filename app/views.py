from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contato    
def index(request):
    lista = Contato.objects.all()
    print(lista)
    context = {
    'lista': lista
    }

    return render(request, "index.html", context)