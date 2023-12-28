from django.contrib import admin
# from .models import Product
from apps.store.models.product import Product
from apps.store.models.common import Discount, Category

admin.site.register(Product)
admin.site.register(Discount)
admin.site.register(Category)
# admin.site.register()
