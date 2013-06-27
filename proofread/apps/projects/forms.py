from datetime import datetime

from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):
    now = datetime.strftime(datetime.now(), "%B %d, %Y %I:%M %p")
    title = forms.CharField(initial=now)

    class Meta:
        model = Project
        fields = ('title', 'unedited')
        widgets = {
            'unedited': forms.Textarea(attrs={
                'cols': 80,
                'rows': 10,
                }),
        }


