from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    empresa = 'Morpheus Corp'
    context = {
        'empresa': empresa
    }

    return render(request, "index.html", context)