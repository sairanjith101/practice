from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

class ProductsView(APIView):

    def get(self, request):
        all_products = Products.objects.all()
        products_data = []
        for product in all_products:
            single_product = {
                'id': product.id,
                'product_name': product.product_name,
                'code': product.code,
                'price': product.price
                }
            products_data.append(single_product)
        return Response(products_data)
    
    def post(self, request):
        new_product = Products(product_name = request.data["product_name"], code = request.data["code"], price = request.data["price"])
        new_product.save()
        return Response("Data Saved")

class ProductsViewById(APIView):

    def get(self, request, id):
        products = Products.objects.get(id = id)
        single_product = {
            'id': products.id,
            'product_name': products.product_name,
            'code': products.code,
            'price': products.price
        }
        print(single_product)
        return Response(single_product)