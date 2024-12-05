from django import forms
from .models import Tasks

class task_creationform(forms.ModelForm):
    class Meta:
        model=Tasks
        fields=['title' , 'completition_status']
    