# Generated by Django 3.2.6 on 2021-09-08 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StackOverflow', '0003_question_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default='def', max_length=50),
            preserve_default=False,
        ),
    ]