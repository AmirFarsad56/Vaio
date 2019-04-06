from django.db import models
from django.conf import settings

class CommonUserModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE,
                               related_name='commonusers', primary_key = True)
    first_name = models.CharField(max_length=216, null = True, blank = False)
    last_name = models.CharField(max_length=216, null = True, blank = False)
    phone_number = models.CharField(max_length = 20, null = True, blank = False )
    picture = models.ImageField(default = r'commonuser/default/coverpicture/default_profile_pic.jpg',
                                 upload_to=r'commonuser/coverpicture')
    #booked_times = models.ForeignKey()


    def __str__(self):
        return self.user.username
