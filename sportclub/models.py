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
    bankaccount_name = models.CharField(max_length = 300, null = True, blank = True)
    bankaccount_number = models.CharField(max_length = 30, null = True, blank = True)
    bankaccount_cardnumber = models.CharField(max_length = 30, null = True, blank = True)
    bankaccount_shabanumber = models.CharField(max_length = 50, null = True, blank = True)
    #later these fields can change to iinteger field if need to
    bankaccount_bankname = models.CharField(max_length = 100, null = True, blank = True)
    #this should be a dropdown menu

    def __str__(self):
        return self.user.username
