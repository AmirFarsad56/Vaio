# Generated by Django 2.1.7 on 2019-05-06 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_usermodel_super_user_logs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='super_user_logs',
            new_name='user_logs',
        ),
    ]