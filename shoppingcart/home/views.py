from django.shortcuts import render
from shopeapp.models import Product

# Create your views here.
def Home(request):
    products=Product.objects.all()
    context={
        'product':products
    }
    return render(request,'home.html',context)

def Cart(request):
    product_id=request.POST.get('pid')
    
    Cart_data=Cart(product_id=product_id)
    cart_data.save()
    return redirect(Home)
