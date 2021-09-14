from django import forms
from .models import Question
from django.contrib.auth.models import User

class userform(forms.ModelForm):
    class Meta:
        model = User
        fields=[
            'username',
            'password',
        ]

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields=[
            'text',
            'tags',
        ]
