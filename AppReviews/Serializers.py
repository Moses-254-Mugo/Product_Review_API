from dataclasses import fields
from pyexpat import model
from .models import Product, Category, Company
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'url']
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']

class ProductSerialier(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['pk', 'name', 'category']

