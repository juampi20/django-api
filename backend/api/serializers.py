from rest_framework import serializers
from .models import *

"""
Serializers are basically used to convert complex data to native Python
datatypes that can then be easily rendered into JSON.
"""

# Create your serializers here.
class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ("id", "name", "alias")