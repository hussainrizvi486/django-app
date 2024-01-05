from rest_framework.viewsets import ViewSet
from apps.store.models.customer import Customer, Cart, CartItem
from apps.store.models.product import Product
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.utils import tree
from decimal import Decimal

# from django.shortcuts import

# from rest_framework.response import


@permission_classes([IsAuthenticated])
class CartApi(ViewSet):
    def add_to_cart(self, request):
        user = request.user
        data: dict = request.data
        product_id = data.get("product_id")
        qty = data.get("qty") or 1
        product = Product.objects.get(id=product_id)

        try:
            customer = Customer.objects.get(user=user)
        except Customer.DoesNotExist:
            return Response("Customer not found")

        cart, created = Cart.objects.get_or_create(customer=customer)
        try:
            cart_item = CartItem.objects.get(item=product, cart=cart)
            cart_item_qty = Decimal(cart_item.qty)
            cart_item.qty += qty
            cart_item.rate = product.price
            cart_item.amount = product.price * cart_item_qty
            cart_item.save()
            # product.cover_image
            # cart.total_qty = cart_item_qty
        except CartItem.DoesNotExist:
            new_cart_item = CartItem.objects.create(
                item=product.id,
                cart=cart.id,
                rate=product.price,
                qty=qty,
                amount=(product.price * qty),
            )
            new_cart_item.save()

        return Response("Cart updated/created")

    def get_cart_detail(self, request):
        user = request.user
        response_obj = {}
        try:
            customer = Customer.objects.get(user=user)
        except Customer.DoesNotExist:
            return Response("Customer not found")

        cart = Cart.objects.filter(customer=customer).first()
        # print(cart.full_clean())
        if not cart:
            return Response(data=[])

        # from django.db import
        # cart_items = list(CartItem.objects.values().filter(cart=cart))
        # cart_items = Cart.objects.raw(
        #     f"""
        #     SELECT
        #         ci.id,
        #         ci.qty,
        #         ci.rate,
        #         p.cover_image,
        #         p.product_name,
        #         ci.amount
        #     FROM
        #         store_cartitem ci
        #     INNER JOIN store_product p on p.id = ci.item_id
        #     WHERE ci.cart_id = '{cart.id}'
        #     """
        # )

        from server.utils import exceute_sql_query

        query = f"""SELECT
                        ci.id,
                        ci.qty,
                        ci.rate,
                        p.cover_image,
                        p.product_name,
                        ci.amount
                    FROM
                        store_cartitem ci
                    INNER JOIN store_product p on p.id = ci.item_id 
                    WHERE ci.cart_id = '{cart.id}'
                    """
        cart_items = exceute_sql_query(query)
        response_obj["items"] = cart_items
        response_obj["total_qty"] = cart.total_qty
        response_obj["total_amount"] = cart.total_amount

        return Response(data=response_obj)


def dictfetchall(cursor):
    """
    Return all rows from a cursor as a dict.
    Assume the column names are unique.
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
