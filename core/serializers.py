# serializers.py
from rest_framework import serializers
from .models import Category, CustomUser, Product
# serializers.py
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
