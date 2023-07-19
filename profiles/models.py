# Create your models here.
from django.db import models
from django.conf import settings


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    profile_pic = models.ImageField(upload_to="profile_pictures/")
    service = models.CharField(max_length=300, blank=True)
    business = models.CharField(max_length=200, blank=True)
    rating = models.PositiveIntegerField(default=100)
