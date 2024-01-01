from django.db import models
from .base import BaseModel
from .product import Product
from .customer import Customer

from apps.accounts.models import User


class Order(BaseModel):
    order_id = models.CharField(max_length=99)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    order_date = models.DateField(auto_now_add=True)
    delivery_date = models.DateField(auto_now_add=True)
    order_status = models.CharField(null=True, blank=True, max_length=99)
    delivery_status = models.CharField(null=True, blank=True, max_length=99)
    payment_status = models.CharField(null=True, blank=True, max_length=99)
    payment_method = models.CharField(null=True, blank=True, max_length=99)
    total_qty = models.FloatField()
    grand_total = models.DecimalField(decimal_places=2, max_digits=12, null=True)

    def __str__(self) -> str:
        return self.order_id


class OrderItems(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.FloatField()
    rate = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=12, null=True)

    def __str__(self) -> str:
        return self.order.order_id
