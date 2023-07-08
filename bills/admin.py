from django.contrib import admin
from .models import Bill, Payed_Bill


admin.site.register(Bill)
admin.site.register(Payed_Bill)