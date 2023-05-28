# babies/views.py
from rest_framework import viewsets
from .models import Baby
from .serializers import BabySerializer

class BabyViewSet(viewsets.ModelViewSet):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer
