from django.urls import path
from .views import *

urlpatterns = [
    path('product/add/', ProductsView.as_view()),
]
