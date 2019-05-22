from jdatetime import date, timedelta
import jdatetime
from django.utils import timezone


def AllSaturdays(length):
   dates = date(jdatetime.datetime.now().year, jdatetime.datetime.now().month, jdatetime.datetime.now().day)    #today
   today = dates
   dates += timedelta(days = 0 - dates.weekday())
   current_month = jdatetime.datetime.now().month
   if (0 - today.weekday()) >= 0:
       yield dates
   if current_month + length > 12:
        new_month = current_month + length - 12
        try:
            f = date(jdatetime.datetime.now().year+1, new_month, jdatetime.datetime.now().day)
        except:
            f = date(jdatetime.datetime.now().year+1, new_month+1, 1)
   else:
        try:
            f = date(jdatetime.datetime.now().year, jdatetime.datetime.now().month+length, jdatetime.datetime.now().day)
        except:
            if jdatetime.datetime.now().month+length == 11:
                f = date(jdatetime.datetime.now().year+1, 1, 1)
            else:
                f = date(jdatetime.datetime.now().year, jdatetime.datetime.now().month+length+1, 1)
   while dates <= f:
       dates += timedelta(days = 7)
       if dates <= f:
           yield dates


def AllSundays(length):
   dates = date(jdatetime.datetime.now().year, jdatetime.datetime.now().month, jdatetime.datetime.now().day)    #today
   today = dates
   dates += timedelta(days = 1 - dates.weekday())
   current_month = jdatetime.datetime.now().month
   if 1 - today.weekday() >= 0:
       yield dates
   if current_month + length > 12:
       new_month = current_month + length - 12
       try:
           f = date(jdatetime.datetime.now().year+1, new_month, jdatetime.datetime.now().day)
       except:
           f = date(jdatetime.datetime.now().year+1, new_month+1, 1)
   else:
       try:
           f = date(jdatetime.datetime.now().year, jdatetime.datetime.now().month+length, jdatetime.datetime.now().day)
       except:
           if jdatetime.datetime.now().month+length == 11:
               f = date(jdatetime.datetime.now().year+1, 1, 1)
           else:
               f = date(jdatetime.datetime.now().year, jdatetime.datetime.now().month+length+1, 1)
   while dates <= f:
      dates += timedelta(days = 7)
      if dates <= f:
          yield dates



def AllMondays(length):
   dates = date(jdatetime.datetime.now().year, jdatetime.datetime.now().month, jdatetime.datetime.now().day)    #today
   today = dates
   dates += timedelta(days = 2 - dates.weekday())
   current_month = jdatetime.datetime.now().month
   if 2 - today.weekday() >= 0:
       yield dates
   if current_month + length > 12:
       new_month = current_month + length - 12
       try:
           f = date(jdatetime.datetime.now().year+1, new_month, jdatetime.datetime.now().day)
       except:
           f = date(jdatetime.datetime.now().year+1, new_month+1, 1)
   else:
       try:
           f = date(jdatetime.datetime.now().year, jdatetime.datetime.now().month+length, jdatetime.datetime.now().day)
       except:
           if jdatetime.datetime.now().month+length == 11:
               f = date(jdatetime.datetime.now().year+1, 1, 1)
           else:
               f = date(jdatetime.datetime.now().year, jdatetime.datetime.now().month+length+1, 1)
   while dates <= f:
      dates += timedelta(days = 7)
      if dates <= f:
          yield dates


def AllTuesdays(length):
   dates = date(jdatetime.datetime.now().year, jdatetime.datetime.now().month, jdatetime.datetime.now().day)    #today
   today = dates
   dates += timedelta(days = 3 - dates.weekday())
   current_month = jdatetime.datetime.now().month
   if 3 - today.weekday() >= 0:
       yield dates
   if current_month + length > 12:
       new_month = current_month + length - 12
       try:
           f = date(jdatetime.datetime.now().year+1, new_month, jdatetime.datetime.now().day)
       except:
           f = date(jdatetime.datetime.now().year+1, new_month+1, 1)
   else:
       try:
           f = date(jdatetime.datetime.now().year, jdatetime.datetime.now().month+length, jdatetime.datetime.now().day)
       except:
           if jdatetime.datetime.now().month+length == 11:
               f = date(jdatetime.datetime.now().year+1, 1, 1)
           else:
               f = date(jdatetime.datetime.now().year, jdatetime.datetime.now().month+length+1, 1)
   while dates <= f:
      dates += timedelta(days = 7)
      if dates <= f:
          yield dates



def AllWednesdays(length):
   dates = date(jdatetime.datetime.now().year, jdatetime.datetime.now().month, jdatetime.datetime.now().day)    #today
   today = dates
   dates += timedelta(days = 4 - dates.weekday())
   current_month = jdatetime.datetime.now().month
   if 4 - today.weekday() >= 0:
       yield dates
   if current_month + length > 12:
       new_month = current_month + length - 12
       try:
           f = date(jdatetime.datetime.now().year+1, new_month, jdatetime.datetime.now().day)
       except:
           f = date(jdatetime.datetime.now().year+1, new_month+1, 1)
   else:
       try:
           f = date(jdatetime.datetime.now().year, jdatetime.datetime.now().month+length, jdatetime.datetime.now().day)
       except:
           if jdatetime.datetime.now().month+length == 11:
               f = date(jdatetime.datetime.now().year+1, 1, 1)
           else:
               f = date(jdatetime.datetime.now().year, jdatetime.datetime.now().month+length+1, 1)
   while dates <= f:
      dates += timedelta(days = 7)
      if dates <= f:
          yield dates


def AllThursdays(length):
   dates = date(jdatetime.datetime.now().year, jdatetime.datetime.now().month, jdatetime.datetime.now().day)    #today
   today = dates
   dates += timedelta(days = 5 - dates.weekday())
   current_month = jdatetime.datetime.now().month
   if 5 - today.weekday() >= 0:
       yield dates
   if current_month + length > 12:
       new_month = current_month + length - 12
       try:
           f = date(jdatetime.datetime.now().year+1, new_month, jdatetime.datetime.now().day)
       except:
           f = date(jdatetime.datetime.now().year+1, new_month+1, 1)
   else:
       try:
           f = date(jdatetime.datetime.now().year, jdatetime.datetime.now().month+length, jdatetime.datetime.now().day)
       except:
           if jdatetime.datetime.now().month+length == 11:
               f = date(jdatetime.datetime.now().year+1, 1, 1)
           else:
               f = date(jdatetime.datetime.now().year, jdatetime.datetime.now().month+length+1, 1)
   while dates <= f:
      dates += timedelta(days = 7)
      if dates <= f:
          yield dates


def AllFridays(length):
   dates = date(jdatetime.datetime.now().year, jdatetime.datetime.now().month, jdatetime.datetime.now().day)    #today
   today = dates
   dates += timedelta(days = 6 - dates.weekday())
   current_month = jdatetime.datetime.now().month
   if 6 - today.weekday() >= 0:
       yield dates
   if current_month + length > 12:
       new_month = current_month + length - 12
       try:
           f = date(jdatetime.datetime.now().year+1, new_month, jdatetime.datetime.now().day)
       except:
           f = date(jdatetime.datetime.now().year+1, new_month+1, 1)
   else:
       try:
           f = date(jdatetime.datetime.now().year, jdatetime.datetime.now().month+length, jdatetime.datetime.now().day)
       except:
           if jdatetime.datetime.now().month+length == 11:
               f = date(jdatetime.datetime.now().year+1, 1, 1)
           else:
               f = date(jdatetime.datetime.now().year, jdatetime.datetime.now().month+length+1, 1)
   while dates <= f:
      dates += timedelta(days = 7)
      if dates <= f:
          yield dates


def TotalMinutes(time):
    total_minutes = (time.hour * 60) + time.minute
    return total_minutes
