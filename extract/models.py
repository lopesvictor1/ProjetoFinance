from django.db import models
from userProfile.models import Category, Account

class Inputs_outputs(models.Model):
    choice_type = (
        ('I', 'Input'),
        ('O', 'Output')
    )
    
    value = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField()
    date = models.DateField()
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=1, choices=choice_type)

    def __str__(self):
        return self.description
