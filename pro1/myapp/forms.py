from django import forms
from .models import noteapp


class NoteForm(forms.ModelForm):

    class Meta:

        model = noteapp

        fields = ['title', 'description','category']

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Title'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Description'
            })

        }