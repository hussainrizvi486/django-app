from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import status


class Product(APIView):
    def get(self, request):
        pass


# class Cart(APIView):
#     def get(self, request):
#         user = self.request.user
#         if user.is_anonymous:
#             return Response({"message": "User is not authenticated", "user": str(self.request.user)})

#         order = Order.objects.filter(user=user.id, ordered=False).first()

#         if not order:
#             return Response({"message": "No active order found"}, status=status.HTTP_404_NOT_FOUND)

#         order_serializer = OrderSerializer(order)
#         order_items = OrderItem.objects.filter(order=order.id)
#         order_items_serailizer = OrderItemSerializers(
#             order_items, many=True)

#         reponse_data = {
#             "order": order_serializer.data,
#             "order_items": order_items_serailizer.data
#         }
#         return Response(reponse_data, status=status.HTTP_200_OK)
