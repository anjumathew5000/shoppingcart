from django.urls import path
from . import views

urlpatterns = [
    path('product_reg',views.ProductRegister,name='product_reg'),
    path('product_reg/<int:pid>',views.ProductRegister,name='product_reg'),
    path('product_list/',views.ProductList,name='product_list'),
    path('product_delete/<int:pid>',views.ProductDelete,name='product_delete'),
    path('product_edit/<int:pid>',views.ProductEdit,name='product_edit'),
    
]
