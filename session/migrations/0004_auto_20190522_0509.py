# Generated by Django 2.1.7 on 2019-05-22 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0003_auto_20190522_0503'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='sessionmodel',
            unique_together=set(),
        ),
    ]