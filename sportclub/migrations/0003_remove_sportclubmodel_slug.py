# Generated by Django 2.1.7 on 2019-04-16 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportclub', '0002_auto_20190416_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sportclubmodel',
            name='slug',
        ),
    ]
