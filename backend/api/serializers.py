from rest_framework import serializers
from .models import Service

class ServiceAll(serializers.ModelSerializer):
    class Meta:
        model = Service  # Corrected from models = Service
        fields = '__all__'  # This includes all fields from the Service model
