from rest_framework import serializers
from .models import noteapp

class noteappSerializer(serializers.ModelSerializer):

    class Meta:
        model = noteapp
        fields = '__all__'