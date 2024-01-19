from django.shortcuts import render
from django.http import HttpResponse


# views.py
# views.py
from rest_framework import generics
from rest_framework import permissions
from .models import Product, Shop
from .serializers import ProductSerializer

class ProductListByShop(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]  # Adjust permissions as needed

    def get_queryset(self):
        shop_name = self.kwargs['shop_name']
        try:
            shop = Shop.objects.get(name=shop_name)
            return Product.objects.filter(shop=shop)
        except Shop.DoesNotExist:
            return Product.objects.none()
# views.py
from rest_framework import generics
from rest_framework import permissions
from .models import Product, Shop, Category
from .serializers import ProductSerializer

class ProductListByShopAndCategory(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]  # Adjust permissions as needed

    def get_queryset(self):
        shop_name = self.kwargs['shop_name']
        category_name = self.kwargs['category_name']

        try:
            shop = Shop.objects.get(name=shop_name)
        except Shop.DoesNotExist:
            return Product.objects.none()

        try:
            category = Category.objects.get(name=category_name, shop_type=shop.shop_type)
        except Category.DoesNotExist:
            return Product.objects.none()

        return Product.objects.filter(shop=shop, category=category)
