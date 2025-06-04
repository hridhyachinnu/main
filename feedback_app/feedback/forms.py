from django import forms
from .models import InternFeedback

class InternFeedbackForm(forms.ModelForm):
    class Meta:
        model = InternFeedback
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'overall_satisfaction': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),
        }
