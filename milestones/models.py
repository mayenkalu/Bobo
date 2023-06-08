from django.db import models
from django.utils import timezone
from django.apps import apps
from babies.models import Baby
from .utils import generate_progress_report


class Milestone(models.Model):
    month = models.IntegerField()
    description = models.TextField()
    area = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class LoggedMilestone(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, related_name='logged_milestones_set')
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE, related_name='logged_milestones')

    def __str__(self):
        return f'{self.baby.name}: {self.milestone.description}'

class Activity(models.Model):
    month = models.IntegerField()
    activity = models.TextField()


class NutritionGuide(models.Model):
    month = models.IntegerField()
    guide = models.TextField()


class Progress(models.Model):
    baby = models.ForeignKey('babies.Baby', on_delete=models.CASCADE, related_name='progresses')
    report = models.TextField()

    def __str__(self):
        return f'Progress for {self.baby.name} at {timezone.now()}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        Baby = apps.get_model('babies', 'Baby')  # get Baby model
        baby = Baby.objects.get(id=self.baby_id)
        baby.progress_report = generate_progress_report(baby.logged_milestones_set.all(), baby.age_in_months)
        baby.save()
