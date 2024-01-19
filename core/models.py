from django.db import models

# Create your models here.
# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class ShopType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    shop_type = models.ForeignKey(ShopType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=255)
    shop_type = models.ForeignKey(ShopType, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    owner = models.ForeignKey('CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    # Add any additional fields you need for your user model
    # For example, you might want to add fields like address, phone number, etc.
    pass
