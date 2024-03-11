from rest_framework import serializers


class TokenObtainPairSerializer(serializers.Serializer):
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    username = serializers.CharField()
    password = serializers.CharField()
