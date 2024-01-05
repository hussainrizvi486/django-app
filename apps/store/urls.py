from django.urls import path
from . import views
from .api.product import ProductApi, ProductDetail
from .api.cart import CartApi


urlpatterns = [
    path("product/details/<str:product_id>", ProductDetail.as_view()),
    path("get-products", ProductApi.as_view()),
    path("add-to-cart", CartApi.as_view({"post": "add_to_cart"})),
    path("get-cart", CartApi.as_view({"get": "get_cart_detail"})),
    # path("user-orders", views.Cart.as_view())
    path("product", views.Product.as_view()),
    path("get-user", views.user.as_view()),
    path("categories", views.CreateCategory.as_view()),
]
