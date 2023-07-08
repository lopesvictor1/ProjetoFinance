from django.db import models
from django.db.models import Sum
from .models import Account

def value_sum(list, column):
    total = list.aggregate(Sum(column)).get(f"{column}__sum")
    return total