from .views import LoginAPIView, LogoutAPIView
from django.urls import path

app_name = "accounts"
urlpatterns = [
    path("", LoginAPIView.as_view(), name="login"),
    path("logout/", LogoutAPIView.as_view(), name="login"),
]
