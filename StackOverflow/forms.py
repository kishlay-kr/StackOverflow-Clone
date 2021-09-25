from django import forms
from .models import Question, Answer, Comment
from django.contrib.auth.models import User

# class userform(forms.ModelForm):
#     class Meta:
#         model = User
#         fields=[
#             'username',
#             'password',
#         ]

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields=[
            'text',
            'tags',
        ]

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields=[
            'text'
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text'
        ]