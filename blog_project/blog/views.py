from rest_framework import viewsets
from blog.serializers import BoardSerializer
from .models import Board

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
