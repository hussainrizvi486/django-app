from django.db import models
from  .base import BaseModel
from  .common import  Category



# brand
class Product(BaseModel):
    product_name = models.CharField(max_length=9999)
    net_price = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    description = models.TextField(default="", null=True)
    stock = models.IntegerField(default=1)
    disabled = models.BooleanField(default=False, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    cover_image = models.CharField(max_length=10000, null=True)
    rating = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.product_name

    # def save(self, *args, **kwargs):
    #     self.net_price = self.price


class ProductImages(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    image_url = models.CharField(max_length=10000)

    def __str__(self) -> str:
        return self.product.product_name
