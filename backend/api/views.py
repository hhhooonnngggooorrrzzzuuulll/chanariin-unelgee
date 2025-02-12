from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *

class ServiceGetCreate(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceAll  # Change from serializers_class to serializer_class

class ServiceUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceAll  # Change from serializers_class to serializer_class

class CategoryGetCreate(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryAll  # Change from serializers_class to serializer_class

class CategoryUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryAll  # Change from serializers_class to serializer_class
