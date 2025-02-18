from rest_framework import serializers
from .models import *

# All fields
class Products_Serializers(serializers.ModelSerializer):
    class Meta:

        model = Products
        fields = '__all__'

# Single Field
class Products_Serializers2(serializers.ModelSerializer):
    class Meta:

        model = Products
        fields = ['product_name']

class Category_Serializer(serializers.ModelSerializer):
    class Meta:

        model = Category
        fields = '__all__'