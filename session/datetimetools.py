from jdatetime import date, timedelta
import jdatetime
from django.utils import timezone


def AllSaturdays(length, start_time = jdatetime.datetime.now()):
   dates = date(start_time.year, start_time.month, start_time.day)    #today
   today = dates
   dates += timedelta(days = 0 - dates.weekday())
   current_month = start_time.month
   if 0 - today.weekday() >= 0:
       yield dates
   if current_month + length > 12:
       new_month = current_month + length - 12
       try:
           f = date(start_time.year+1, new_month, start_time.day)
       except:
           f = date(start_time.year+1, new_month+1, 1)
   else:
       try:
           f = date(start_time.year, start_time.month+length, start_time.day)
       except:
           if start_time.month+length == 11:
               f = date(start_time.year+1, 1, 1)
           else:
               f = date(start_time.year, start_time.month+length+1, 1)
   while dates <= f:
      dates += timedelta(days = 7)
      if dates <= f:
          yield dates


def AllSundays(length, start_time = jdatetime.datetime.now()):
   dates = date(start_time.year, start_time.month, start_time.day)    #today
   today = dates
   dates += timedelta(days = 1 - dates.weekday())
   current_month = start_time.month
   if 1 - today.weekday() >= 0:
       yield dates
   if current_month + length > 12:
       new_month = current_month + length - 12
       try:
           f = date(start_time.year+1, new_month, start_time.day)
       except:
           f = date(start_time.year+1, new_month+1, 1)
   else:
       try:
           f = date(start_time.year, start_time.month+length, start_time.day)
       except:
           if start_time.month+length == 11:
               f = date(start_time.year+1, 1, 1)
           else:
               f = date(start_time.year, start_time.month+length+1, 1)
   while dates <= f:
      dates += timedelta(days = 7)
      if dates <= f:
          yield dates


def AllMondays(length, start_time = jdatetime.datetime.now()):
   dates = date(start_time.year, start_time.month, start_time.day)    #today
   today = dates
   dates += timedelta(days = 2 - dates.weekday())
   current_month = start_time.month
   if 2 - today.weekday() >= 0:
       yield dates
   if current_month + length > 12:
       new_month = current_month + length - 12
       try:
           f = date(start_time.year+1, new_month, start_time.day)
       except:
           f = date(start_time.year+1, new_month+1, 1)
   else:
       try:
           f = date(start_time.year, start_time.month+length, start_time.day)
       except:
           if start_time.month+length == 11:
               f = date(start_time.year+1, 1, 1)
           else:
               f = date(start_time.year, start_time.month+length+1, 1)
   while dates <= f:
      dates += timedelta(days = 7)
      if dates <= f:
          yield dates


def AllTuesdays(length, start_time = jdatetime.datetime.now()):
   dates = date(start_time.year, start_time.month, start_time.day)    #today
   today = dates
   dates += timedelta(days = 3 - dates.weekday())
   current_month = start_time.month
   if 3 - today.weekday() >= 0:
       yield dates
   if current_month + length > 12:
       new_month = current_month + length - 12
       try:
           f = date(start_time.year+1, new_month, start_time.day)
       except:
           f = date(start_time.year+1, new_month+1, 1)
   else:
       try:
           f = date(start_time.year, start_time.month+length, start_time.day)
       except:
           if start_time.month+length == 11:
               f = date(start_time.year+1, 1, 1)
           else:
               f = date(start_time.year, start_time.month+length+1, 1)
   while dates <= f:
      dates += timedelta(days = 7)
      if dates <= f:
          yield dates


def AllWednesdays(length, start_time = jdatetime.datetime.now()):
   dates = date(start_time.year, start_time.month, start_time.day)    #today
   today = dates
   dates += timedelta(days = 4 - dates.weekday())
   current_month = start_time.month
   if 4 - today.weekday() >= 0:
       yield dates
   if current_month + length > 12:
       new_month = current_month + length - 12
       try:
           f = date(start_time.year+1, new_month, start_time.day)
       except:
           f = date(start_time.year+1, new_month+1, 1)
   else:
       try:
           f = date(start_time.year, start_time.month+length, start_time.day)
       except:
           if start_time.month+length == 11:
               f = date(start_time.year+1, 1, 1)
           else:
               f = date(start_time.year, start_time.month+length+1, 1)
   while dates <= f:
      dates += timedelta(days = 7)
      if dates <= f:
          yield dates


def AllThursdays(length, start_time = jdatetime.datetime.now()):
   dates = date(start_time.year, start_time.month, start_time.day)    #today
   today = dates
   dates += timedelta(days = 5 - dates.weekday())
   current_month = start_time.month
   if 5 - today.weekday() >= 0:
       yield dates
   if current_month + length > 12:
       new_month = current_month + length - 12
       try:
           f = date(start_time.year+1, new_month, start_time.day)
       except:
           f = date(start_time.year+1, new_month+1, 1)
   else:
       try:
           f = date(start_time.year, start_time.month+length, start_time.day)
       except:
           if start_time.month+length == 11:
               f = date(start_time.year+1, 1, 1)
           else:
               f = date(start_time.year, start_time.month+length+1, 1)
   while dates <= f:
      dates += timedelta(days = 7)
      if dates <= f:
          yield dates


def AllFridays(length, start_time = jdatetime.datetime.now()):
   dates = date(start_time.year, start_time.month, start_time.day)    #today
   today = dates
   dates += timedelta(days = 6 - dates.weekday())
   current_month = start_time.month
   if 6 - today.weekday() >= 0:
       yield dates
   if current_month + length > 12:
       new_month = current_month + length - 12
       try:
           f = date(start_time.year+1, new_month, start_time.day)
       except:
           f = date(start_time.year+1, new_month+1, 1)
   else:
       try:
           f = date(start_time.year, start_time.month+length, start_time.day)
       except:
           if start_time.month+length == 11:
               f = date(start_time.year+1, 1, 1)
           else:
               f = date(start_time.year, start_time.month+length+1, 1)
   while dates <= f:
      dates += timedelta(days = 7)
      if dates <= f:
          yield dates


def TotalMinutes(time):
    total_minutes = (time.hour * 60) + time.minute
    return total_minutes
