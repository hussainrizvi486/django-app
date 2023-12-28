from django.urls import path
from django.http import JsonResponse
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .api.register import RegisterUser



def index(request):
    return JsonResponse("accounts", safe=False)


urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register_user'),

    path('auth-token/', views.AccountsTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('auth-token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
