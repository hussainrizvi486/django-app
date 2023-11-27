from rest_framework.serializers import ModelSerializer
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name",
                  "email", "phone_number", "password"]


class AccountsTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # token['id'] = user.id
        token['username'] = user.username
        token['email'] = user.email
        return token
