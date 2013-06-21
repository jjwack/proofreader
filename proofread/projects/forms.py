from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title', 'unedited')
        widgets = {
            'unedited': forms.Textarea(attrs={
                'cols': 80,
                'rows': 10,
                }),
        }

