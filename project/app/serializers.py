from rest_framework import serializers
from .models import *

class sample(serializers.Serializer):
    roll=serializers.IntegerField()
    name=serializers.CharField()
    place=serializers.CharField()
