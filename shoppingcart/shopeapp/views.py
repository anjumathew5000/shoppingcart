from django.shortcuts import render
from .models import Product

# Create your views here.
def ProductRegister(request):
    if request.method == 'POST':
        product_name=request.POST.get('pname')
        product_price=request.POST.get('pprice')
        product_quantity=request.POST.get('pquantity')
        product_image=request.FILES['pimage']
        product_status=request.POST.get('pstatus')
        if product_status == "0":
            p_status="In-stock"
        else:
            p_status="out of stock"
        product=Product(product_name=product_name,
                        product_quantity=product_quantity,
                        product_price=product_price,
                        product_image=product_image,
                        product_status= p_status)
        product.save()

    return render(request,"product_reg.html")
def ProductList(request):
    return render(request,"product_list.html")