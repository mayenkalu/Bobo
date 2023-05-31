from django import forms
from babies.models import Baby

class MilestoneLogForm(forms.ModelForm):
    class Meta:
        model = Baby
        fields = ['logged_milestones']
