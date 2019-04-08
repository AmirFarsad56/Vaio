from django.db import models
from django.conf import settings


class SportClubModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE,
                                primary_key = True, related_name = 'sportclubs')
    phone_number = models.CharField(max_length = 20, blank = False)
    address = models.TextField(blank = False)
    info = models.TextField(blank = True, null= True)
    picture = models.ImageField(default = r'sportclub/default/coverpicture.png',
                                 upload_to=r'sportclub/coverpicture')

    def __str__(self):
        return self.user.username
