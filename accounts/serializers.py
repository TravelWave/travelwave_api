import re

from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            "full_name",
            "phone_number",
            "is_driver",
            "driver_license",
            "password",
        ]

    def create(self, validated_data):
        phone_number = validated_data.pop("phone_number")
        password = validated_data.pop("password")
        user = CustomUser.objects.create_user(
            phone_number,
            password,
            **validated_data,
        )
        return user

    def validate_phone_number(self, value):
        pattern = r"^(?:\+\d{3})?\d{10}$"

        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "wrong phone number format.",
            )
