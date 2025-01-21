from django.db import models

# Create your models here.

class Category(models.Model):
    Cname = models.CharField(max_length=50)

    def __str__(self):
        return self.Cname

class Books(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=False, blank=False)
    title = models.CharField(max_length=50, null=False, blank=False)
    author = models.CharField(max_length=50)
    publication = models.CharField(max_length=50)
    pbn = models.CharField(max_length=50)
    pages = models.IntegerField()

    def __str__(self):
        return self.title
