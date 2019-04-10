from django.db import models
from sportclub.models import SportClubModel

class SalonModel(models.Model):
    sportclub = models.ForeignKey(SportClubModel, on_delete = models.CASCADE,
                                  related_name = 'salons')

    area = models.CharField(max_length=264, blank=False)
    floor_type = models.CharField(max_length = 264, blank = True, null = True)
    locker = models.BooleanField(blank = False)
    drinking_water = models.BooleanField(blank = False)
    parking_area = models.BooleanField(blank = False)
    shower = models.PositiveIntegerField(blank = False)
    changing_room = models.PositiveIntegerField(blank = False)


class SalonPictureModel(models.Model):
    salon = models.ForeignKey(SalonModel, on_delete = models.CASCADE,
                               related_name = 'pictures')
    picture = models.ImageField(blank = True, null = True,
                                upload_to=r'sportclub/salon/picture')
