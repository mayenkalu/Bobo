from django.db import models
from django.utils import timezone
from django.db import models
from babies.models import Baby
# import BabyProfile model

class Milestone(models.Model):
    month = models.IntegerField()
    description = models.TextField()
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.logged:
            for baby in Baby.objects.filter(logged_milestones__id=self.id):
                baby.update_progress()

class Activity(models.Model):
    month = models.IntegerField()
    activity = models.TextField()

class NutritionGuide(models.Model):
    month = models.IntegerField()
    guide = models.TextField()

class Progress(models.Model):
    baby = models.OneToOneField(Baby, on_delete=models.CASCADE)
    report = models.TextField()

    def __str__(self):
        return f'Progress for {self.baby.name} at {timezone.now()}'