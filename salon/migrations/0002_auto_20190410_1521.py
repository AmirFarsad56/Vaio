# Generated by Django 2.1.7 on 2019-04-10 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salonpicturemodel',
            old_name='Salon',
            new_name='salon',
        ),
        migrations.AlterField(
            model_name='salonmodel',
            name='floor_type',
            field=models.CharField(blank=True, max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='salonpicturemodel',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='sportclub/salon/picture'),
        ),
    ]