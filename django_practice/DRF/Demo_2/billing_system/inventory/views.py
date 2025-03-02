from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class ProductView(APIView):

    # with serializer
    def get(self, request):
        all_products = Products.objects.all()
        serialized_product = Product_Serializers2(all_products, many=True).data
        return Response(serialized_product) 

    # without serializer
    # def get(self, request):
    #     all_products = Products.objects.all()
    #     product_data = []
    #     for product in all_products:
    #         single_product = {
    #             'id': product.id,
    #             'product_name': product.product_name,
    #             'code': product.code,
    #             'price': product.price
    #         }
    #         product_data.append(single_product)
    #     print(product_data)
    #     return Response(product_data)

    def post(self, request):
        new_product = Products(product_name = request.data['product_name'], code = request.data['code'], price = request.data['price'], category_reference_id = request.data['category_reference_id'])
        new_product.save()
        return Response("Data Saved")
    
class ProductViewById(APIView):

    # with serializer
    def get(self, request, id):
        product = Products.objects.get(id = id)
        single_product = Product_Serializers2(product).data
        return Response(single_product)

    # without serializer
    # def get(self, request, id):
    #     product = Products.objects.get(id = id)
    #     single_product = {
    #         "id": product.id,
    #         'product_name': product.product_name,
    #         'code': product.code,
    #         'price': product.price
    #     }
    #     print(single_product)
    #     return Response(single_product)

    def patch(self, request, id):
        product = Products.objects.filter(id = id)
        product.update(product_name = request.data['product_name'], code = request.data['code'], price = request.data['price'])
        return Response("Updated")
    
    def delete(self, request, id):
        product = Products.objects.get(id = id)
        product.delete()
        return Response("Deleted")

class CategoryView(APIView):

    def post(self, request):
        new_category = Category(category_name = request.data['category_name'])
        new_category.save()
        return Response("Data Saved")
    
class CategoryViewById(APIView):

    def delete(self, request, id):
        category_data = Category.objects.get(id=id)
        category_data.delete()
        return Response("Deleted")
    
