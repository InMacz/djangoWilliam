from django.db import models

class Contato(models.Model):
    Nome = models.CharField(max_length=50, blank=False, null=False, help_text='Informe seu nome')
    Email = models.CharField(max_length=100, blank=False, null=False, help_text='Informe seu e-Mail')
    DtaNas = models.DateField()
# Create your models here.
