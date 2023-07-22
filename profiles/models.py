# Create your models here.
from django.db import models
from django.conf import settings


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    profile_pic = models.ImageField(upload_to="profile_pictures/")
    business = models.CharField(max_length=200, blank=True)
    rating = models.PositiveIntegerField(default=100)
    location = models.CharField(max_length=200, blank=True)
    miles = models.CharField(max_length=200, blank=True)
    phonenumber = models.CharField(max_length=20, blank=True)
    owner_full_name = models.CharField(max_length=200, blank=True)
    linkxdate = models.FileField(upload_to="linkxdate", blank=True)
    docs = models.FileField(upload_to="docs")
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.user.username
