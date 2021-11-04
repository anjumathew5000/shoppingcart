from django.shortcuts import render,redirect
from shopeapp.models import Product,Cart

# Create your views here.
def Home(request):
    products=Product.objects.all()
    datacount=Cart.objects.all().count()
    context={
        'product':products,
        'datacount':datacount
    }
   
    return render(request,'home.html',context)

def Cart_data(request):
    print("hii")
    if request.method =="POST":
        product_id=request.POST.get('pid')
        print(product_id)
        # if Cart.objects.filter(product_id=product_id).exists():
        #     return render(request,'home.html',{"message":'already added'})
        data=Product.objects.get(id=product_id)
        print(data)
        Cart_data=Cart(product_id=data)
        Cart_data.save()

        return redirect(Home)
def cart_list(request):
    data=Cart.objects.all()
    return render(request,'cart_list.html',{"data":data})
