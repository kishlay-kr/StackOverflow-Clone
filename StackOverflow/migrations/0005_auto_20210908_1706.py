# Generated by Django 3.2.6 on 2021-09-08 11:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('StackOverflow', '0004_question_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='upvotes_ans',
            field=models.ManyToManyField(blank=True, null=True, related_name='upvotes_ans', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='upvotes_ques',
            field=models.ManyToManyField(blank=True, null=True, related_name='upvotes_ques', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='views',
            field=models.ManyToManyField(blank=True, null=True, related_name='views', to=settings.AUTH_USER_MODEL),
        ),
    ]
