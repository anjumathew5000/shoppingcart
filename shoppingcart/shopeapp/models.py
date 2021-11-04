from django.db import models

# Create your models here.

class Product(models.Model):
    product_name=models.CharField(max_length=50)
    product_quantity=models.IntegerField()
    product_price=models.CharField(max_length=50)
    product_image=models.ImageField(upload_to='images/')
    product_status=models.CharField(max_length=50)
class Cart(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE,default=True)
    