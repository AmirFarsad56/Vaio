from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class UserModel(AbstractUser):
    first_name = models.CharField(max_length=216, null = False, blank = False)
    last_name = models.CharField(max_length=216, null = False, blank = False)
    is_sportclub = models.BooleanField('SportClub Status', default = False)
    is_commonuser = models.BooleanField('CommonUser Status', default = False)
    is_masteruser = models.BooleanField('MasterUser Status', default = False)
    email = models.EmailField(unique = True, blank = False)
