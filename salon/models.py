from django.db import models
from sportclub.models import SportClubModel

class SalonModel(models.Model):

    sportclub = models.ForeignKey(SportClubModel, on_delete = models.CASCADE,
                                  related_name = 'salons')
    is_confirmed = models.BooleanField(default = False,
                                       null = False)
    area = models.CharField(max_length=264, blank=False, null = False)
    floor_type = models.CharField(max_length = 264, blank = True, null = True)
    locker = models.BooleanField(blank = False, null = False)
    drinking_water = models.BooleanField(blank = False, null = False)
    parking_area = models.BooleanField(blank = False, null = False)
    shower = models.PositiveIntegerField(blank = False, null = False)
    changing_room = models.PositiveIntegerField(blank = False, null = False)
    is_futsall = models.BooleanField(blank = False, null = False)
    is_volleyball = models.BooleanField(blank = False, null = False)
    is_football = models.BooleanField(blank = False, null = False)
    is_basketball = models.BooleanField(blank = False, null = False)

    def __str__(self):
        name = str(self.area)+' square meters'
        return name

    def confirm(self):
        self.is_confirmed = True
        self.save()

    def ban(self):
        self.is_confirmed = False
        self.save()    




class SalonPictureModel(models.Model):
    salon = models.ForeignKey(SalonModel, on_delete = models.CASCADE,
                               related_name = 'pictures')
    picture = models.ImageField(blank = True, null = True,
                                upload_to=r'sportclub/salon/picture')
