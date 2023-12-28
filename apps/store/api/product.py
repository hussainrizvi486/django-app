from rest_framework import viewsets
from apps.store.models.product import Product


class ProductApi(viewsets.ViewSet):
    def get_produts(self, request):
        product = Product.objects.all()
    ...