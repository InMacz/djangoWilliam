from django import forms

from .models import Contato

class ContatoModelForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['Nome', 'Email', 'DtaNas']
            