from django.urls import path
from . import views


urlpatterns = [
    # path("user-orders", views.Cart.as_view())
    path("product", views.Product.as_view())
]
