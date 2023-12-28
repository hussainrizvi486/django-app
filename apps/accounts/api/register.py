from rest_framework.views import APIView
from apps.accounts.models import User
from django.core.validators import validate_email
from django.http import HttpResponseBadRequest
from rest_framework.response import  Response


class RegisterUser(APIView):
    def post(self, request):
        user_object = request.data
        print(request)
        print(user_object)
        # user_object = self.validate_user_object(user_object)

        user = User.objects.create(
            first_name=user_object.get("first_name"),
            last_name=user_object.get("last_name"),
            username=user_object.get("username"),
            password=user_object.get("password"),
            email=user_object.get("email"),
            phone_number=user_object.get("phone_number")
        )

        user.save()
        return Response({"message": "user create"})

    def validate_user_object(self, user_object: dict):
        required_fields = [
            "first_name",
            "last_name",
            "username",
            "phone_number",
            "email",
            "password",
        ]

        for key in user_object.items():
            if key not in required_fields:
                raise Exception(f"{key} is missing")

        if not self.validate_email(user_object.get("email")):
            raise Exception("email is not vaild")
        
        if len(user_object.get("phone")) < 8:
            raise Exception("Password is to short")


        return user_object

    def validate_email(self, email):
        "first we have validate email with RE"

        user = User.objects.filter(email=email)
        
        if user:
            raise Exception("email already taken")
        
        return True


