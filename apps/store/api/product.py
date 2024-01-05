from rest_framework.views import APIView
from apps.store.models.product import Product, ProductImages
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ProductDetail(APIView):
    def get(self, request, product_id):
        data = {}
        product = get_object_or_404(Product, id=product_id)
        if product:
            data = dict(Product.objects.values().filter(id=product_id)[0])
            pi = list(
                ProductImages.objects.values("image_url").filter(product=product_id)
            )

            # print(images)
            images = []
            data["price"] = '{:20,.2f}'.format(data["price"])
            if pi:
                for image in pi:
                    images.append(image.get("image_url"))

                data["images"] = images
        return Response(status=200, data=data)


class ProductApi(APIView):
    def get(self, request):
        products = Product.objects.values(
            "id", "product_name", "price", "cover_image", "category"
        )[:50]
        return Response(status=200, data=products)

    def create_product(self, request):
        product_object = {
            "product_name": "",
            "price": 0,
            "description": "",
            "stock": 0,
            "disabled": "",
            "category": "",
            "cover_images": "",
        }

        product = Product.objects.create(
            product_name=product_object.get("product_name"),
            net_price=product_object.get("net_price"),
            price=product_object.get("price"),
            description=product_object.get("description"),
            stock=product_object.get("stock"),
            disabled=product_object.get("disabled"),
            category=product_object.get("category"),
            cover_images=product_object.get("cover_images"),
        )
        product.save()
        ...
