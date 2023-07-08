from django.urls import path
from . import views

urlpatterns = [
    path('set_bills/', views.set_bills, name='set_bills'),
    path('show_bills/', views.show_bills, name='show_bills')
]