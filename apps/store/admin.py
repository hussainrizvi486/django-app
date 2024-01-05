from django.contrib import admin

# from .models import Product
from apps.store.models.product import Product, ProductImages
from apps.store.models.common import Discount, Category
from apps.store.models.customer import Customer, Cart, CartItem
from apps.store.models.order import Order, OrderItems


class ProductImageInline(admin.TabularInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    # model = Product
    inlines = [
        ProductImageInline,
    ]
    search_fields = ["product_name", "category", "price"]


admin.site.register(Product, ProductAdmin)

admin.site.register(Discount)
admin.site.register(Category)


admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(CartItem)

# admin.site.register()
