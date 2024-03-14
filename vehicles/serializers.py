from rest_framework import serializers

from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            "driver",
            "name",
            "make",
            "model",
            "year",
            "color",
            "license_plate",
            "number_of_seats",
        ]
