from django.shortcuts import render
from rest_framework import viewsets
from .models import Mail
from serializers import MailSerializer

class MailViewSet(viewsets.ModelViewSet):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer

