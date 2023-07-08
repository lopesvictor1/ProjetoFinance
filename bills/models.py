from django.db import models
from userProfile.models import Category
from django.utils import timezone
import datetime

# Create your models here.

class Bill(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=200)
    value = models.FloatField(default=0)
    payment_day = models.IntegerField(default=1)

    def __str__(self):
        return self.title
    
    def payment(self):
        return str(self.payment_day)
    
class Payed_Bill(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.DO_NOTHING)
    payed = models.DateField()

    def __str__(self):
        return self.bill.title