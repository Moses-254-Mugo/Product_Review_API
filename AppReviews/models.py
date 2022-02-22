from itertools import product
from nturl2path import url2pathname
from tkinter import CASCADE
from typing import OrderedDict
from unicodedata import category, name
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    url = models.TextField()

    def __str__(self):
        return self.name

class ProductSize(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name =models.CharField(max_length=100)
    content = models.TextField()
    category = models.ManyToManyField(Category, related_name='products')
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    class Meta: 
        ordering = ['-created']
    
    def __str__(self):
        return self.name

class ProductSite(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sites', related_query_name='site')
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='sites', related_query_name='site')
    productsize = models.ForeignKey(ProductSize, on_delete=models.CASCADE, related_name='sites', related_query_name='site')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    url = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments',related_query_name='comment')
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
