from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from djrichtextfield.models import RichTextField
from multiselectfield import MultiSelectField




My_Tags = (('python','python'),
           ('django','django'),
           ('cpp','cpp'),
           ('C','C'),
           ('HTML','HTML'),
           ('CSS','CSS'),
           ('javascript','javascript'),
           ('other','other'))



class Question(models.Model):
    title = models.CharField(max_length=50)
    text = RichTextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    views = models.ManyToManyField(User, related_name = 'views', null=True, blank=True)
    upvotes_ques = models.ManyToManyField(User,related_name = 'upvotes_ques', null=True, blank=True)
    created_at = models.DateField(auto_now_add = True)
    n_comments = models.IntegerField( default=0)
    n_answers = models.IntegerField(default=0)
    tags = MultiSelectField(choices=My_Tags, default='other')

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = RichTextField()
    upvotes_ans = models.ManyToManyField(User, related_name = 'upvotes_ans', null=True, blank=True)
    question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name = 'question_ans')
    author_ans = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user_ans')

class Comment(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question , null=True, blank = True, related_name = 'question_cmnt', on_delete = models.CASCADE)
    answer = models.ForeignKey(Answer, null = True, blank = True, related_name = 'answer',on_delete = models.CASCADE) ## trying to make a single comments model for both question ans answers, will make separate models for if any problem arises.
    author_cmnt = models.ForeignKey(User, related_name = 'user_cmnt', on_delete = models.CASCADE) #related name is used to refer back to the model e.g. User.Comments .
    time  = models.DateField(auto_now_add = True)



