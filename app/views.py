from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contato
from .forms import ContatoModelForm    
def index(request):
    lista = Contato.objects.all()
    print(lista)
    context = {
    'lista': lista
    }

    return render(request, "index.html", context)

def consContato(request, pk):
    contato = Contato.objects.get(id = pk)
    context = {
        'contato': contato
    }
    return render(request, "consContato.html", context)

def cadContato(request):

    if request.method == 'POST':
        form = ContatoModelForm(request.POST)

        if form.is_valid():
            contato = form.save(commit=False)

            print(f"Nome: {contato.Nome}")
            print(f"Email: {contato.Email}")
            print(f"Data de Nascimento: {contato.DtaNas}")

            messages.success(request, 'Contato cadastrado com sucesso!')
        else:
            messages.error(request, "Erro ao cadastrar contato")
    else:
        form = ContatoModelForm()

    context = {
        'form': form
    }

    return render(request, 'cadContato.html', context)
