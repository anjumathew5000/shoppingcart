from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.Home,name='home'),
    path('cart/',views.Cart_data,name='cart'),
    path('cart_list/',views.cart_list,name='cart_list')
   
   
    
]