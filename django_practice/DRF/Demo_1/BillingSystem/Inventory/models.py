from django.db import models

# Create your models here.

class Products(models.Model):
    product_name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    price = models.FloatField(default=0)