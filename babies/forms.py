from django import forms
from .models import Baby

class BabyForm(forms.ModelForm):
    class Meta:
        model = Baby
        widgets = {
          'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
          'weight': forms.NumberInput(attrs={'placeholder': 'Kilograms'}),
          'height': forms.NumberInput(attrs={'placeholder': 'Centimeters'}),
        }
        fields = ['name', 'gender', 'picture', 'date_of_birth', 'weight', 'height', 'parent_name', 'parent_relationship']
