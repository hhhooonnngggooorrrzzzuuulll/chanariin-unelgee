from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Service
from .serializers import ServiceAll

class ServiceGetCreate(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceAll  # Change from serializers_class to serializer_class

class ServiceUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceAll  # Change from serializers_class to serializer_class
