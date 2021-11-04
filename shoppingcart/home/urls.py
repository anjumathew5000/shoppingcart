from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.Home,name='home'),
    path('cart/',views.Cart,name='cart')
   
   
    
]