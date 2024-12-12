from django.db import models
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.name
