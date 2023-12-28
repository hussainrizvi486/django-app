from django.urls import path
from . import views
from .api.product import ProductApi


urlpatterns = [
    path("get-products", ProductApi.as_view()),
    # path("user-orders", views.Cart.as_view())
    path("product", views.Product.as_view()),
    path("categories", views.CreateCategory.as_view())

]
