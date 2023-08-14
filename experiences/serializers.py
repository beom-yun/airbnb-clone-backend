from rest_framework.serializers import ModelSerializer
from .models import Experience, Perk


class PerkSerializer(ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"
