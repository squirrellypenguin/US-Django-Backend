from .models import Event, User
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [ "id", "title", "summary", "url"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [ "id", "username", "password", "email"]