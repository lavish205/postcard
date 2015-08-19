from rest_framework import serializers, viewsets
from .models import User

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ( 'id', 'url', 'email', 'is_staff', 'password', 'last_login')