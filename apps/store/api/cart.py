from rest_framework.viewsets import ViewSet
from apps.store.models.customer import Customer, Cart, CartItem
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


# @permission_classes([IsAuthenticated])
class CartApi(ViewSet):
    def add_to_cart(self, request):
        user = request.user
        print(self.request.user)
        # customer = get_object_or_404(Customer, user=user) or None
        # if customer:
        #     cart = get_object_or_404(Cart, customer=customer) or None
        #     if not cart:
        #         cart = Cart.objects.create(customer=customer)

        return Response("cart created")

    ...
