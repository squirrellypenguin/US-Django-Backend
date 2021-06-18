from .models import Event
from rest_framework import serializers
from django.contrib.auth.models import User, Group
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [ "id", "title", "summary", "url", 'user']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "url", "groups"]

class GroupsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        field = ['url', 'name']