# Generated by Django 2.1.7 on 2019-04-19 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SportClubModel',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='sportclubs', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('info', models.TextField(blank=True, null=True)),
                ('picture', models.ImageField(default='sportclub/default/coverpicture.png', upload_to='sportclub/coverpicture')),
                ('bankaccount_name', models.CharField(blank=True, max_length=300, null=True)),
                ('bankaccount_number', models.CharField(blank=True, max_length=30, null=True)),
                ('bankaccount_cardnumber', models.CharField(blank=True, max_length=30, null=True)),
                ('bankaccount_shabanumber', models.CharField(blank=True, max_length=50, null=True)),
                ('bankaccount_bankname', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
