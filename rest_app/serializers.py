from rest_framework import serializers
from .models import HomeApi

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeApi
        fields = ('serial_number', 'name', 'surname', 'city', 'mobile')
