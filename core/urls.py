
from django.urls import path
from .views import *

urlpatterns = [
    #
   path('api/products/<str:shop_name>/', ProductListByShop.as_view(), name='product-list-by-shop'),
   path('api/products/<str:shop_name>/<str:category_name>/', ProductListByShopAndCategory.as_view(), name='product-list-by-shop-and-category'),
 path('api/categories/<str:shop_name>/', CategoryListByShop.as_view(), name='category-list-by-shop'),


]
