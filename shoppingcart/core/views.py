from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from shopeapp.views import ProductList


# Create your views here.
def UserRegister(request):
    try:
        if request.method == "POST":
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            first_name=request.POST.get('firstname')
            last_name=request.POST.get('lastname')
            user=User(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
            user.save()
            return render(request,'login.html')
    except Exception:
         return render(request,'userreg.html')
    return render(request,'userreg.html')
def UserLogin(request):
    print("yesssss")
    if request.method == "POST":
        username=request.POST.get('email')
        password=request.POST.get('password')
        print(username)
        print(password)
        if User.objects.filter(email=username,password=password).exists():
            print("yessssssssss")
            return redirect(ProductList)
        else:
            return render(request,"login.html",{'message':"invalid username or passsword"})