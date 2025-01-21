from django.urls import path, include
from bookStation import views

urlpatterns = [
    path('', views.home, name='home'),

]
