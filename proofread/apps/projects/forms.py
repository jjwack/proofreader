from datetime import datetime

from django import forms

from .models import Project


def get_time():
    return datetime.strftime(datetime.now(), "%B %d, %Y %I:%M %p")


class ProjectForm(forms.ModelForm):
    title = forms.CharField(initial=get_time())

    class Meta:
        model = Project
        fields = ('title', 'unedited')
        widgets = {
            'unedited': forms.Textarea(attrs={
                'cols': 80,
                'rows': 10,
                }),
        }


