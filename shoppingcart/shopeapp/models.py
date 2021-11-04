from django.db import models

# Create your models here.

class Product(models.Model):
    product_name=models.CharField(max_length=50)
    product_quantity=models.IntegerField()
    product_price=models.CharField(max_length=50)
    product_image=models.ImageField(upload_to='images/')
    product_status=models.CharField(max_length=50)