# Create your models here.
from django.db.models import CharField, EmailField, BooleanField, DateTimeField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .manager import UserManager


class Account(AbstractBaseUser, PermissionsMixin):
    username = CharField(unique=True, max_length=200, blank=True, null=True)
    email = EmailField(blank=True, null=True)
    phone = CharField(null=True, blank=True, max_length=10)
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=True)
    is_admin = BooleanField(default=False)
    date_joined = DateTimeField(default=timezone.now)
    last_login = DateTimeField(null=True)
    objects = UserManager()
    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
