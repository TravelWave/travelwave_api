from rest_framework import serializers

from accounts.models import CustomUser

from .models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    ride = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        required=False,
    )
    passenger = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        required=False,
    )
    driver = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        required=False,
    )

    class Meta:
        model = Feedback
        fields = [
            "ride",
            "passenger",
            "driver",
            "rating",
            "sos_notification",
            "feedback",
        ]

    def create(self, validated_data):
        if validated_data.get("sos_notification"):
            # TODO: send notification to the admin of the system
            pass

        return super().create(**validated_data)
