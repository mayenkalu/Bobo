from rest_framework import viewsets
from .models import Milestone, LoggedMilestone, Activity, NutritionGuide, Progress
from .serializers import MilestoneSerializer, LoggedMilestoneSerializer, ActivitySerializer, NutritionGuideSerializer, ProgressSerializer

class MilestoneViewSet(viewsets.ModelViewSet):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer

class LoggedMilestoneViewSet(viewsets.ModelViewSet):
    queryset = LoggedMilestone.objects.all()
    serializer_class = LoggedMilestoneSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class NutritionGuideViewSet(viewsets.ModelViewSet):
    queryset = NutritionGuide.objects.all()
    serializer_class = NutritionGuideSerializer

class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer