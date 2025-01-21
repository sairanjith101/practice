from django.shortcuts import render
from .models import Category, Books

# Create your views here.

def home(request):
    category = Category.objects.all()
    books = Books.objects.all()
    return render(request, 'bookStation/index.html', {'book':books, 'category': category})