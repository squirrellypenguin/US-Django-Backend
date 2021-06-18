from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Event
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import EventSerializer, UserSerializer, GroupsSerializer, EventUserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (JWTAuthentication, )

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
        return Event.objects.filter(user=id)