# Generated by Django 2.1.7 on 2019-05-31 23:02

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0008_auto_20190531_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='lastdatamodel',
            name='first_day_2',
            field=django_jalali.db.models.jDateField(blank=True, null=True),
        ),
    ]
