from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

class ProductsView(APIView):
    def post(self, request):
        print(request.data)
        return Response("Data Saved")