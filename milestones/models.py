from django.db import models

from django.db import models
from babies.models import Baby  # import BabyProfile model

class Milestone(models.Model):
    month = models.IntegerField()
    description = models.TextField()

class Activity(models.Model):
    month = models.IntegerField()
    activity = models.TextField()

class NutritionGuide(models.Model):
    month = models.IntegerField()
    guide = models.TextField()
