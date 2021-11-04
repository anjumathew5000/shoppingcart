from django.urls import path
from . import views

urlpatterns = [
    path('',views.UserRegister,name='user_reg'),
    path('userlogin',views.UserLogin,name='userlogin'),
   
    
]