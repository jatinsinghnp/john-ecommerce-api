# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.basemodel import BaseModel
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

# from django.core.validators import


User = get_user_model()


# Create your models here.
def validate_dimensions(value):
    """
    Ensure that the value is properly formatted as three comma-separated integers.
    """
    parts = value.split(",")
    if len(parts) != 3:
        raise ValidationError("Dimensions must be three comma-separated integers.")
    try:
        int(parts[0])
        int(parts[1])
        int(parts[2])
    except ValueError:
        raise ValidationError("Dimensions must be three comma-separated integers.")


class Product(BaseModel):
    class Quantity(models.TextChoices):
        BULK = "bulk", _("bulk")
        ITEM = "item", _("item")
        DEFAULT = "", _("")

    class Condition(models.TextChoices):
        NEW = "new", _("new")
        USED = "used", _("used")
        DEFAULT = "", _("")

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    title = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    color = models.ManyToManyField("Color", related_name="colors")
    quantity_choose = models.CharField(
        max_length=10, choices=Quantity.choices, default=Quantity.DEFAULT
    )
    condition = models.CharField(
        max_length=10, choices=Condition.choices, default=Condition.DEFAULT
    )
    include = models.ManyToManyField("Includes", related_name="includes")
    product_images = models.ManyToManyField("Images", blank=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)
    WEIGHT_UNIT_CHOICES = (
        ("kg", "kilograms"),
        ("lbs", "pounds"),
        ("gm", "grams"),
    )
    weight_unit = models.CharField(
        max_length=5, choices=WEIGHT_UNIT_CHOICES, default="kg"
    )
    dimensions = models.CharField(max_length=30, validators=[validate_dimensions])
    is_digital = models.BooleanField(default=False)
    is_pickup = models.BooleanField(default=False)
    expedite_cost = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True
    )
    size = models.CharField(max_length=200)
    delivery_time_1_2_day = models.PositiveIntegerField(null=True, blank=True)
    delivery_time_2_3_day = models.PositiveIntegerField(null=True, blank=True)
    delivery_time_3_5_day = models.PositiveIntegerField(null=True, blank=True)
    delivery_time_1_week = models.PositiveIntegerField(null=True, blank=True)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0, blank=True
    )
    fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Color(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Includes(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Images(BaseModel):
    image = models.FileField(upload_to="product/")
