# Generated by Django 2.1.7 on 2019-04-16 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masteruser', '0003_auto_20190416_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masterusermodel',
            name='slug',
        ),
    ]
