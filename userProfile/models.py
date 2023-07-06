from django.db import models

# Create your models here.
from django.contrib import admin

class Category(models.Model):
    name = models.CharField(max_length=200)
    isEssencial = models.BooleanField(default=False)
    intended_value = models.FloatField(default=0)


    def __str__(self):
        return self.name


class Account(models.Model):

    banks = (('NU', 'Nubank'), ('BB', 'Banco do Brasil'), ('CE', 'Caixa Economica'), ('IT', 'Itau'), ('SI', 'Sicredi'))
    types = (('PF', 'Pessoa Física'), ('PJ', 'Pessoa Juridica'))
    name = models.CharField(max_length=200)
    bank = models.CharField(max_length=2, choices=banks)
    type = models.CharField(max_length=2, choices=types)
    value = models.FloatField(default = 0)
    icon = models.ImageField(upload_to='icones')

    def __str__(self):
        return self.name



