from django.urls import path
from applications.account.views import UserRegisterAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/',  UserRegisterAPIView.as_view()),
    path('login/',  TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view())
]