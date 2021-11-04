from django.shortcuts import render,redirect
from .models import Product

# Create your views here.
def ProductRegister(request,pid=None):
    if pid:
        product=Product.objects.get(id=pid)
        return render(request,"product_reg.html",{'product':product})
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
        
        return redirect(ProductList)

    return render(request,"product_reg.html")
def ProductList(request):
    product=Product.objects.all()
    context={
        "product":product
    }
    return render(request,"product_list.html",context)
def ProductDelete(request,pid):
    print(pid)
    product=Product.objects.filter(id=pid)
    product.delete()
    return redirect(ProductList)
def ProductEdit(request,pid):
    if request.method =="POST":
        product_name=request.POST.get('pname')
        product_price=request.POST.get('pprice')
        product_quantity=request.POST.get('pquantity')
        try:
            product_image=request.FILES['pimage']
        except Exception:
            product_image=Product.objects.get(id=pid).product_image
        product_status=request.POST.get('pstatus')
        if product_status == "0":
            p_status="In-stock"
        else:
            p_status="out of stock"
        product=Product.objects.filter(id=pid).update(product_name=product_name,
                        product_quantity=product_quantity,
                        product_price=product_price,
                        product_image=product_image,
                        product_status= p_status)
        return redirect(ProductList)