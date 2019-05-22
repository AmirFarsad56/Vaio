from django.db import models
from django_jalali.db import models as jmodels
from salon.models import SalonModel
from django.utils.text import slugify
from django.conf import settings

class SessionModel(models.Model):
    salon = models.ForeignKey(SalonModel, on_delete = models.CASCADE,
                                  related_name = 'sessions',blank = False,
                                  null = False)
    booker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE,
                               related_name='sessions', blank = True, null = True)
    day = jmodels.jDateField(null = True)
    time = models.TimeField(null = True)
    duration = models.CharField(max_length = 264, blank = False , null = False)
    price = models.IntegerField(blank = True, null = True)
    is_booked = models.BooleanField(blank = False, default = False)
    is_ready = models.BooleanField(blank = False, default = False)



    def save(self, *args, **kwargs):
        if self.price:
            self.is_ready = True
        super(SessionModel, self).save(*args, **kwargs)
'''
199271Raiden
'''
