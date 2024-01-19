from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(CustomUser)
# admin.site.register(CartItem)
# admin.site.register(Cart)
admin.site.register(Shop)
admin.site.register(ShopType)
admin.site.register(Category)
admin.site.register(Product)
