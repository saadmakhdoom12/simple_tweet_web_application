from django import forms
from .models import Tweet


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'What\'s happening?',
                'rows': 3,
                'class': 'form-control',
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
            }),
        }
        labels = {
            'text': '',
            'photo': 'Add a photo',
        }
        help_texts = {
            'text': 'Max 280 characters',
        }
        error_messages = {
            'text': {
                'max_length': 'This tweet is too long.',
            },
        }
