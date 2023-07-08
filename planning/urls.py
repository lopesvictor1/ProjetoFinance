from django.urls import path
from . import views

urlpatterns = [
    path('set_planning/', views.set_planning, name='set_planning'),
    path('update_category_value/<str:pk>', views.update_category_value, name='update_category_value'),
    path('see_planning/', views.see_planning, name='see_planning'),
]