# Generated by Django 3.2.6 on 2021-09-08 11:12

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('StackOverflow', '0002_auto_20210901_0234'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tags',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('python', 'python'), ('django', 'django'), ('cpp', 'cpp'), ('C', 'C'), ('HTML', 'HTML'), ('CSS', 'CSS'), ('javascript', 'javascript'), ('other', 'other')], default='other', max_length=45),
        ),
    ]
