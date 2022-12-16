from rest_framework.serializers import ModelSerializer
from .models import Room, Amenity


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"
