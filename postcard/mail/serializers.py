__author__ = 'lavish'
from .models import Mail
from rest_framework import serializers

class MailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mail
        fields = ('subject',)