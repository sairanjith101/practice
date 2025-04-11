from django.db import models

# Create your models here.

class ProductView(models.Model):
    product_name = models.CharField(max_length=200, null=True)
    code = models.CharField(max_length=200, null = True)
    price = models.FloatField(default=0)