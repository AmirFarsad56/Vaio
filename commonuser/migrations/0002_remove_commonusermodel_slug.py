# Generated by Django 2.1.7 on 2019-04-21 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commonuser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commonusermodel',
            name='slug',
        ),
    ]
