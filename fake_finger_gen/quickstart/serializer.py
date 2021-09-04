from rest_framework import serializers
from .models import HandImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HandImage
        fields = "__all__"
