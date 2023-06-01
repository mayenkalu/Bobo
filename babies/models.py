from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import date
from dateutil.relativedelta import relativedelta
from milestones.utils import generate_progress_report
from django.apps import apps
#from milestones.models import Progress


# Create your models here


class Baby(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=50, choices=[('Male', 'Male'), ('Female', 'Female')], null=True)
    picture = models.ImageField(upload_to='baby_pictures/', blank=True, null=True)
    date_of_birth = models.DateField(null=False)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    parent_name = models.CharField(max_length=200, null=True)
    parent_relationship = models.CharField(max_length=200, null=False)
    logged_milestones = models.ManyToManyField('milestones.Milestone', blank=True, related_name='babies')
    progress = models.ForeignKey('milestones.Progress', on_delete=models.CASCADE, null=True, related_name='babies')



    @property
    def age_in_months(self):
        from dateutil.relativedelta import relativedelta
        from datetime import date
        rdelta = relativedelta(date.today(), self.date_of_birth)
        return rdelta.years * 12 + rdelta.months

    def update_progress(self):
        Progress = apps.get_model('milestones', 'Progress')
        progress, created = Progress.objects.get_or_create(baby=self)
        logged_milestones = self.logged_milestones.all()
        progress.report = generate_progress_report(logged_milestones, self.age_in_months)
        progress.save()

    def __str__(self):
        return self.name
