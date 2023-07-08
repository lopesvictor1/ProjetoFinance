from django.urls import path
from . import views


urlpatterns = [

    path('home/', views.profileHome, name='home'),
    path('manage/', views.profileManage, name='manage'),
    path('register_account/', views.register_account, name='register_account'),
    path('delete_account/<str:pk>', views.delete_account, name='delete_account'),
    path('create_category/', views.create_category, name='create_category'),
    path('update_cateogry/<str:pk>', views.update_category, name='update_category')


]