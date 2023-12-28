from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import status
import requests
from apps.store.models.product import Product as ProductM

# https://crm.paytusker.us/api/resource/Item%20Group?fields=[%22name%22,%20%22image%22]&limit=1000

class Product(APIView):
    def get(self, request):
        req = requests.get(f"""https://crm.paytusker.us/api/resource/Item?fields=[%22name%22,%20%22item_name%22,%20%22item_group%22,%20%22custom_website_price%22,%20%22custom_rating%22,%20%22image%22]&limit=9999""")

        if req:
            data = req.json()
            data = data.get("data")
            print(type(data))
            no_image_url = "https://t4.ftcdn.net/jpg/04/73/25/49/360_F_473254957_bxG9yf4ly7OBO5I0O5KABlN930GwaMQz.jpg"
            products= ProductM.objects.all()
            products.delete()

            for row in data:
                print(row)
                {'name': 'WI-2023-12-00001', 'item_name': 'TEst Item', 'item_group': 'Cameras', 'custom_website_price': 130.0, 'custom_rating': 0.0, 'image': None}
                img = no_image_url
                if row.get("image"):
                    img = f'crm.paytusker.us{row.get("image")}'
                
                product = ProductM.objects.create(
                    product_name = row.get("item_name"), 
                    cover_images = img, 
                    rating = row.get('custom_rating'),
                    price = row.get('custom_website_price') 
                    )
                product.save()
                
            return Response({"status": data})
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
