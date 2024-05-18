from django import forms
from .models import Hackathon

class HackathonForm(forms.ModelForm):
    class Meta:
        model = Hackathon
        fields = ['name', 'start_date', 'end_date', 'description', 'rules']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
