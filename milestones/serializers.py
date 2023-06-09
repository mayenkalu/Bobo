from rest_framework import serializers
from .models import Milestone, LoggedMilestone, Activity, NutritionGuide, Progress

class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = '__all__'

class LoggedMilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoggedMilestone
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class NutritionGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionGuide
        fields = '__all__'

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = '__all__'
