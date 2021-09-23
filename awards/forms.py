from django import forms
from .models import Image, Project


class ImageForm(forms.ModelForm):
    """Form for the image model"""

    class Meta:
        model = Image
        fields = ('title', 'image')


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'author', 'description', 'technologies', 'pic']
