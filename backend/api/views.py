from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, authentication, permissions
from .serializers import *
from .models import *

# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    serializer_class = HeroSerializer
    queryset = Hero.objects.all()
