# Generated by Django 2.1.7 on 2019-04-16 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
