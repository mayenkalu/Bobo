from django import forms
from .models import Baby, Milestone
from milestones.models import Milestone, LoggedMilestone
from django.forms import CheckboxSelectMultiple


class MilestoneLogForm(forms.ModelForm):
    logged_milestones = forms.ModelMultipleChoiceField(
        queryset=Milestone.objects.none(),
        widget=CheckboxSelectMultiple(),
        required=False
    )

    class Meta:
        model = Baby
        fields = ['logged_milestones']

    def __init__(self, *args, **kwargs):
        baby = kwargs.pop('baby', None)
        grouped_milestones = kwargs.pop('grouped_milestones', None)
        super().__init__(*args, **kwargs)
        if baby:
            self.fields['logged_milestones'].queryset = Milestone.objects.filter(month=baby.age_in_months)
        if grouped_milestones:
            self.grouped_milestones = grouped_milestones

    def save(self, commit=True):
        baby = self.instance
        logged_milestones = self.cleaned_data['logged_milestones']
        if commit:
            LoggedMilestone.objects.filter(baby=baby).exclude(milestone__in=logged_milestones).delete()
            for milestone in logged_milestones:
                LoggedMilestone.objects.get_or_create(baby=baby, milestone=milestone)
        return baby
