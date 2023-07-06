from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

admin.site.register(models.Account)
admin.site.register(models.Category)
# Register your models here.
