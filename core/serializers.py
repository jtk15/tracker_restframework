from django.contrib.auth.models import Group, User
from rest_framework import serializers

from core.models import State


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
        
class StateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = State
        fields = ['name', 'abbreviation']