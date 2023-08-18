from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Room, Amenity
from categories.serializers import CategorySerializer
from users.serializers import TinyUserSerializer
from medias.serializers import PhotoSerializer
from wishlists.models import Wishlist


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


class RoomDetailSerializer(ModelSerializer):
    owner = TinyUserSerializer(read_only=True)
    amenities = AmenitySerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)
    rating = SerializerMethodField()
    is_owner = SerializerMethodField()
    is_liked = SerializerMethodField()
    photos = PhotoSerializer(read_only=True, many=True)

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user

    def get_is_liked(self, room):
        request = self.context["request"]
        return Wishlist.objects.filter(user=request.user, rooms__pk=room.pk).exists()

    class Meta:
        model = Room
        fields = "__all__"


class RoomListSerializer(ModelSerializer):
    rating = SerializerMethodField()
    is_owner = SerializerMethodField()
    photos = PhotoSerializer(read_only=True, many=True)

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user

    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_owner",
            "photos",
        )
