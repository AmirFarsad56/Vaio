# Generated by Django 2.1.7 on 2019-05-21 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessionmodel',
            name='slug',
        ),
    ]