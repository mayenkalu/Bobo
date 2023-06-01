from django import forms
from babies.models import Baby
from .models import Milestone  # Import Milestone

class MilestoneLogForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.baby = kwargs.pop('baby', None)  # Get baby from kwargs
        super().__init__(*args, **kwargs)
        if self.baby:
            # Filter milestones by the age of the baby
            self.fields['logged_milestones'].queryset = Milestone.objects.filter(month=self.baby.age_in_months)
    
    class Meta:
        model = Baby
        fields = ['logged_milestones']
