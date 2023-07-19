from .views import LoginAPIView
from django.urls import path

app_name = "accounts"
urlpatterns = [
    path("", LoginAPIView.as_view(), name="login"),
]
