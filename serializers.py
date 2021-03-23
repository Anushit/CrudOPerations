from rest_framework import serializers
from .models import artist

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = artist
        fields = "__all__"