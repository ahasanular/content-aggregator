from rest_framework import serializers
from podcasts.models import Episode


class EpisodeSerializer(serializers.ModelSerializer):
    is_favorite = serializers.BooleanField(read_only=True)

    class Meta:
        model = Episode
        fields = '__all__'