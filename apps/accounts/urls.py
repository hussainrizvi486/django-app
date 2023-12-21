from django.urls import path
from django.http import JsonResponse
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


def index(request):
    return JsonResponse("accounts", safe=False)


urlpatterns = [
    path("auth-register/", views.Register.as_view()),

    path('auth-token/', views.AccountsTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('auth-token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
