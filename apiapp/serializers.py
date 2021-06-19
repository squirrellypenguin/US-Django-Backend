from .models import Event, Picture
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from rest_framework import serializers
import django.contrib.auth.password_validation as validators
from django.contrib.auth import get_user_model
from django.core import exceptions
from rest_framework_jwt.settings import api_settings
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [ "id", "title", "summary", "url", 'user', 'lat', 'long']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name',)
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


# UserModel = get_user_model()


# class UserSerializer(serializers.ModelSerializer):

#     password = serializers.CharField(write_only=True)
#     token = serializers.SerializerMethodField()

#     def get_token(self, obj):
#         jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#         jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

#         payload = jwt_payload_handler(obj)
#         token = jwt_encode_handler(payload)
#         return token

#     def validate(self, data):
#         password = data.get('password')
#         errors = dict()
#         try:
#             validators.validate_password(password=password)

#         # the exception raised here is different than serializers.ValidationError
#         except exceptions.ValidationError as e:
#             errors['password'] = list(e.messages)

#         if errors:
#             raise serializers.ValidationError(errors)

#         return super(UserSerializer, self).validate(data)

#     def create(self, validated_data):

#         user = UserModel.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email']
#         )
#         user.set_password(validated_data['password'])
#         user.save()

#         return user

#     class Meta:
#         model = UserModel
#         fields = ('username', 'email', 'password', 'token')


class GroupsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        field = ['url', 'name']

class EventUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = [ "id", "title", "summary", "url", 'user', 'lat', 'long']

class PictureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Picture
        field = ['title', 'image', 'event']        