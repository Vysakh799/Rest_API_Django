from rest_framework import serializers
from .models import *

class sample(serializers.Serializer):
    roll=serializers.IntegerField()
    name=serializers.CharField()
    place=serializers.CharField()

class model_serializers(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'