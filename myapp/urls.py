from django.urls import path
from . import views

urlpatterns = [
    path('create_client/', views.create_client, name='create_client'),
    path('delete_client/', views.delete_client, name='delete_client'),
    path('get_client/', views.get_client, name='get_client'),
    path('update_client/', views.update_client, name='update_client'),
    path('create_product/', views.create_product, name='create_product'),
    path('delete_product/', views.delete_product, name='delete_product'),
    path('get_product/', views.get_product, name='get_product'),
    path('update_product/', views.update_product, name='update_product'),
    path('create_order/', views.create_product, name='create_order'),
    path('delete_order/', views.delete_product, name='delete_order'),
    path('get_order/', views.get_product, name='get_order'),
    path('update_order/', views.update_product, name='update_order'),
]