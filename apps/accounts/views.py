from .serializers import AccountsTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
import json
from django.http import JsonResponse
from django.core.validators import EmailValidator
from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.decorators import api_view
from .models import User


class SignUp(APIView):
    def get(self, request):
        return JsonResponse({"message": "Register User"})

    def post(self, request):
        request_data: dict = request.data
        first_name = request_data.get("first_name")
        last_name = request_data.get("last_name")
        email = request_data.get("email")
        phone = request_data.get("phone")
        username = request_data.get("username")
        password = request_data.get("password")

        if not first_name:
            return JsonResponse({"message": "first name required"})

        if not last_name:
            return JsonResponse({"message": "last name required"})

        if not email:
            return JsonResponse({"message": "email required"})

        if not phone:
            return JsonResponse({"message": "phone required"})

        if not password:
            return JsonResponse({"message": "password required"})

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            phone_number=phone,
            password=password,
        )
        user.save()

        if user:
            return JsonResponse({"message": "user created successfully", "success": True})

        return JsonResponse({"message": "error while creating user", })


@api_view(['GET'])
def validte_email(request):
    email = request.GET.get("email")
    if User.objects.filter(email=email).exists():
        return Response({"message": "email already exists", "valid": False})

    else:
        return Response({"message": "email not exists", "valid": True})


@api_view(['GET'])
def validte_username(request):
    username = request.GET.get("username")
    if User.objects.filter(username=username).exists():
        return Response({"message": "username already exists", "valid": False})
    else:
        return Response({"message": "username not exists", "valid": True})


class AccountsTokenObtainPairView(TokenObtainPairView):
    serializer_class = AccountsTokenObtainPairSerializer

