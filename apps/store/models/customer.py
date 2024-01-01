from django.db import models
from .base import BaseModel
from .product import Product
from apps.accounts.models import User


class Customer(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=999)

    def __str__(self) -> str:
        return self.customer_name


class Cart(BaseModel):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    total_qty = models.DecimalField(
        decimal_places=2, max_digits=12, null=True, default=0
    )
    total_amount = models.DecimalField(
        decimal_places=2, max_digits=12, null=True, default=0
    )

    def __str__(self) -> str:
        return self.customer.customer_name


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.FloatField(default=1)
    rate = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=12, null=True)

    # def __str__(self) -> str:
