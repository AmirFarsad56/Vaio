from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class UserModel(AbstractUser):
    is_sportclub = models.BooleanField('ClubOwner Status', default = False)
    is_commonuser = models.BooleanField('CommonUser Status', default = False)
    email = models.EmailField(unique = True, blank = False)




