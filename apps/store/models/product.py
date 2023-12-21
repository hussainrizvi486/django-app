from django.db import models
from .base import BaseModel
from .store_models import Category


# brand
class Product(BaseModel):
    product_name = models.CharField(max_length=9999)
    net_price = models.DecimalField(decimal_places=2, max_digits=12)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    description = models.TextField(default="", null=True)
    stock = models.IntegerField(default=1)
    disabled = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    cover_images = models.CharField(max_length=10000, null=True)
    rating = models.IntegerField()


    def save(self):
        self.net_price = self.price

class ProductImages(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    image_url = models.CharField(max_length=10000)

    def __str__(self) -> str:
        return self.product.name
    

class Discount(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount_percentage = models.DecimalField(decimal_places=2, max_digits=5)
    start_date = models.DateField()
    end_date = models.DateField()

    
