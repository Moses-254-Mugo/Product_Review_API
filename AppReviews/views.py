from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .Serializers import ProductSerialier

# Create your views here.
class ProductViewSet(APIView):
    def get(self, request, format=None):
        all_products = Product.objects.all() #Getting all values
        serializers = ProductSerialier(all_products, many=True)
        return Response(serializers. data, status=200)
    
    def post(self, request,format=None):
        serializers = ProductSerialier(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializers.errors, status=400)

class ProductDescription(APIView): #handle entry-specif operations
    def get_products(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            
            return Response({"error": "Not found."}, status=404)
        
    def get(self, request, pk, format=None):
        prod = self.get_products(pk)
        serializers = ProductSerialier(prod)
        return Response(serializers. data)

    def put(self, request, pk=None):
        prod = self.get_products(pk)
        serializers = Product(prod, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=400)
    
    def delete(self, request, pk, format=None):
        prod = self.get_products(pk)
        serializers = ProductSerialier(prod)
        prod.delete()
        return Response(serializers,status=204)