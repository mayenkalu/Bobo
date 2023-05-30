from django import forms
from babies.models import BabyProfile

class MilestoneLogForm(forms.ModelForm):
    class Meta:
        model = BabyProfile
        fields = ['logged_milestones']
