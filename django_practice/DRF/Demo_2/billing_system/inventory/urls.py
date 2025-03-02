from django.urls import path
from .views import *

urlpatterns = [
    path('product/add', ProductView.as_view()),
    path('product/<int:id>', ProductViewById.as_view()),

    path('category', CategoryView.as_view()),
    path('category/<int:id>', CategoryViewById.as_view()),
]
