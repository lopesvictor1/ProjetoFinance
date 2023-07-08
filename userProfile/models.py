from django.db import models
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=200)
    isEssencial = models.BooleanField(default=False)
    planning_value = models.FloatField(default=0)


    def __str__(self):
        return self.name

    def monthly_total(self):
        from extract.models import Inputs_outputs
        ios = Inputs_outputs.objects.filter(category__id=self.id).filter(date__month=datetime.now().month).filter(type='O')
        total = 0
        for io in ios:
            total += io.value
        return total
    
    def percentual_of_planned(self):
        return int((self.monthly_total()*100)/self.planning_value)


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



