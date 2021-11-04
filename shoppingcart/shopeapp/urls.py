from django.urls import path
from . import views

urlpatterns = [
    path('product_reg',views.ProductRegister,name='product_reg')
    
]
