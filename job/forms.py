from django import forms
from .models import ApplyJob


class ApplyForm(forms.ModelForm):
    class Meta:
        model = ApplyJob
        fields = '__all__'
        exclude = 'job','user'