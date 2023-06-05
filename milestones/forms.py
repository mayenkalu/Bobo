from django import forms
from .models import Baby, Milestone

class MilestoneLogForm(forms.ModelForm):
    logged_milestones = forms.ModelMultipleChoiceField(
        queryset=Milestone.objects.none(),
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )

    class Meta:
        model = Baby
        fields = ['logged_milestones']

    def __init__(self, *args, **kwargs):
        baby = kwargs.pop('baby', None)
        grouped_milestones = kwargs.pop('grouped_milestones', None)  # Add this line
        super().__init__(*args, **kwargs)
        if baby:
            self.fields['logged_milestones'].queryset = Milestone.objects.filter(month=baby.age_in_months)
        if grouped_milestones:  # Add this condition
            self.grouped_milestones = grouped_milestones  # Assign the grouped_milestones data to the form



