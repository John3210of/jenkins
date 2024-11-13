from rest_framework import serializers
from .models import Board
class BoardSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S") 
    class Meta:
        model = Board
        fields = '__all__'  # 모든 필드를 포함
