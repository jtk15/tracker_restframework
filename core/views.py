from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, generics

from core.models import City, State
from core.serializers import CitySerializer, GroupSerializer, UserSerializer, StateSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
        
        
class StateAPIView(generics.ListCreateAPIView):
    
    queryset = State.objects.all()
    serializer_class = StateSerializer
    
class StateByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = State.objects.all()
    serializer_class = StateSerializer


class CityAPIView(generics.ListCreateAPIView):
    
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityByIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = City.objects.all()
    serializer_class = CitySerializer

    