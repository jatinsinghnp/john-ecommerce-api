from django.contrib import admin
from .models import Images, Product, Color

# Register your models here.
admin.site.register([Images, Product, Color])
