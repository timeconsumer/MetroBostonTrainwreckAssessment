from rest_framework import serializers
from .models import TrainLine

class TrainLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainLine
        fields = '__all__'
