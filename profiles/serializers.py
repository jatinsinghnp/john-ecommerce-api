from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = (
            "user",
            "profile_pic",
            "business",
            "rating",
            "location",
            "miles",
            "phonenumber",
            "owner_full_name",
            "linkxdate",
            "email",
            "data",
        )

    def get_data(self, obj):
        return obj.data
