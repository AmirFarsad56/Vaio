# Generated by Django 2.1.7 on 2019-05-09 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190506_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='user_logs',
            field=models.TextField(default='', null=True),
        ),
    ]