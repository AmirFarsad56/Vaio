from django.db import models
from django_jalali.db import models as jmodels
from salon.models import SalonModel
from django.utils.text import slugify
from django.conf import settings
from jdatetime import timedelta

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

class LastDataModel(models.Model):
    salon = models.ForeignKey(SalonModel, on_delete = models.CASCADE,
                              related_name = 'lastdatas', blank = False,
                              null = False)
    last_length = models.IntegerField(null = True, blank = True)
    first_day = jmodels.jDateField(null = True, blank = True)
    first_day_2 = jmodels.jDateField(null = True, blank = True)
    last_day = jmodels.jDateField(null = True, blank = True)
    last_saturday = jmodels.jDateField(null = True, blank = True)
    last_sunday = jmodels.jDateField(null = True, blank = True)
    last_monday = jmodels.jDateField(null = True, blank = True)
    last_tuesday = jmodels.jDateField(null = True, blank = True)
    last_wednesday = jmodels.jDateField(null = True, blank = True)
    last_thursday = jmodels.jDateField(null = True, blank = True)
    last_friday = jmodels.jDateField(null = True, blank = True)
    last_saturday_2 = jmodels.jDateField(null = True, blank = True)
    last_sunday_2 = jmodels.jDateField(null = True, blank = True)
    last_monday_2 = jmodels.jDateField(null = True, blank = True)
    last_tuesday_2 = jmodels.jDateField(null = True, blank = True)
    last_wednesday_2 = jmodels.jDateField(null = True, blank = True)
    last_thursday_2 = jmodels.jDateField(null = True, blank = True)
    last_friday_2 = jmodels.jDateField(null = True, blank = True)

    def save(self, *args, **kwargs):
        if self.last_saturday is not None and self.last_sunday is not None and self.last_monday is not None and self.last_tuesday is not None and self.last_wednesday is not None and self.last_thursday is not None and self.last_friday is not None:
            self.first_day_2 = self.last_day + timedelta(days = 1)
            self.first_day = None
            self.last_day = None
            self.last_length = None
            self.last_saturday_2 = self.last_saturday
            self.last_saturday = None
            self.last_sunday_2 = self.last_sunday
            self.last_sunday = None
            self.last_monday_2 = self.last_monday
            self.last_monday = None
            self.last_tuesday_2 = self.last_tuesday
            self.last_tuesday = None
            self.last_wednesday_2 = self.last_wednesday
            self.last_wednesday = None
            self.last_thursday_2 = self.last_thursday
            self.last_thursday = None
            self.last_friday_2 = self.last_friday
            self.last_friday = None
        super(LastDataModel, self).save(*args, **kwargs)
