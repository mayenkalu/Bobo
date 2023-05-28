from django import forms
from .models import Baby

class BabyForm(forms.ModelForm):
    class Meta:
        model = Baby
        widgets = {
          'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
          'weight': forms.TextInput(attrs={'placeholder': 'Kilograms'}),
          'height': forms.TextInput(attrs={'placeholder': 'Centimeters'}),
        }
        fields = ['name', 'gender', 'picture', 'date_of_birth', 'weight', 'height', 'parent_name', 'parent_relationship']
