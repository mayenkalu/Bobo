from django.db import models
from django.utils import timezone
from django.db import models
from babies.models import Baby
# import BabyProfile model

class Milestone(models.Model):
    month = models.IntegerField()
    description = models.TextField()
    logged_by_babies = models.ManyToManyField(Baby, blank=True, related_name='milestones')
    
    def __str__(self):
        return self.description


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.logged_by_babies.exists():  # check if there are any logged babies
            for baby in self.logged_by_babies.all():  # loop through logged babies
                baby.update_progress()  # call update_progress on each baby



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