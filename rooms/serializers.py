from rest_framework.serializers import ModelSerializer
from .models import Room, Amenity


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"
