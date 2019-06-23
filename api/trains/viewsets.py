from rest_framework import viewsets
from .models import TrainLine
from .serializers import TrainLineSerializer

class TrainViewSet(viewsets.ModelViewSet):
    queryset = TrainLine.objects.all()
    serializer_class = TrainLineSerializer
