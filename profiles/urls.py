from django.urls import path
from .views import ProfileUpdateAPIView, ProfileRetrieveAPIView

urlpatterns = [
    path("", ProfileRetrieveAPIView.as_view(), name="profile"),
    path("update/", ProfileUpdateAPIView.as_view(), name="profile-update"),
]
