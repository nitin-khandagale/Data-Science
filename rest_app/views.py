from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HomeSerializer
from .models import HomeApi

class HomeViewSet(viewsets.ModelViewSet):
	queryset = HomeApi.objects.all()
	serializer_class = HomeSerializer
