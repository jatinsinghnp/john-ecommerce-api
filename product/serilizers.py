from rest_framework import serializers
from .models import Product, Color, Includes, Images


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ["id", "name"]


class IncludesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Includes
        fields = ["id", "name"]


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ["id", "image"]


class ProductSerializer(serializers.ModelSerializer):
    color = ColorSerializer(many=True)
    include = IncludesSerializer(many=True)
    product_images = ImagesSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"
