from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Event
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import EventSerializer, UserSerializer, GroupsSerializer, EventUserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
# Create your views here.
import cloudinary.uploader
import cloudinary.api

from .serializers import UserSerializer
class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = (JWTAuthentication, )

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupsSerializer
    permission_classes = [permissions.IsAuthenticated]    

class EventUserList(generics.ListAPIView):
    serializer_class = EventUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (JWTAuthentication, )
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        id = self.kwargs['id']
        print(id)
        return Event.objects.filter(user_id=id)



class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer

class UploadView(APIView):
    # authentication_classes = (TokenAuthentication)
    authentication_classes = (JWTAuthentication, )
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )

    @staticmethod
    def post(request):
        print(request)
        file = request.data.get('picture')
        title = request.data.get('title')
        summary = request.data.get('summary')
        user = request.data.get('user_id')
        print(title, summary, user,)
        user_obj = User.objects.get(id=user)
        print(user_obj)
        upload_data = cloudinary.uploader.upload(file)
        url = upload_data['url']
        Event.objects.create(title = title, summary = summary, url = url, user_id = user_obj)
        return Response({
            'status': 'success',
            'data': upload_data,
        }, status=201)
    