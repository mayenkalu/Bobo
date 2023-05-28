# babies/serializers.py
from rest_framework import serializers
from .models import Baby

class BabySerializer(serializers.ModelSerializer):
    class Meta:
        model = Baby
        fields = '__all__'
