# Generated by Django 3.2.6 on 2021-09-25 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StackOverflow', '0008_auto_20210913_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]