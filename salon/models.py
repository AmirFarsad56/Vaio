from django.db import models
from sportclub.models import SportClubModel

class SalonModel(models.Model):
    sportclub = models.ForeignKey(SportClubModel, on_delete = models.CASCADE,
                                  related_name = 'salons')
    area = models.CharField(max_length=264, blank=False)
    floor_type = models.CharField(max_length = 264, blank = True) 
    locker = models.BooleanField(blank = False)
    drinking_water = models.BooleanField(blank = False)
    parking_area = models.BooleanField(blank = False)
    showers = models.IntegerField(blank = False)
    changing_room = models.IntegerField(blank = False)
    picture = models.ImageField(blank = True , upload_to=r'sportclub/salon/picture')