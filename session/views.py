from django.shortcuts import render
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, get_list_or_404
from jdatetime import date, timedelta
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
import jdatetime
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

#handmade
from session.forms import DaysForm, TimesForm
from session.models import SessionModel
from salon.models import SalonModel
from sportclub.decorators import sportclub_required
from session.datetimetools import (AllSaturdays, AllSundays, AllMondays,
                                AllTuesdays, AllWednesdays, AllThursdays,
                                AllFridays, TotalMinutes)


@login_required
@sportclub_required
def SessionCreateView(request, pk):
    if request.method == 'POST':
        days_form = DaysForm(data = request.POST )
        times_form = TimesForm(data = request.POST )
        if times_form.is_valid() and days_form.is_valid():
            salon_instance = get_object_or_404(SalonModel, pk = pk)
            length = days_form.cleaned_data['length']
            saturdays = days_form.cleaned_data['saturdays']
            sundays = days_form.cleaned_data['sundays']
            mondays = days_form.cleaned_data['mondays']
            tuesdays = days_form.cleaned_data['tuesdays']
            wednesdays = days_form.cleaned_data['wednesdays']
            thursdays = days_form.cleaned_data['thursdays']
            fridays = days_form.cleaned_data['fridays']
            start_time = times_form.cleaned_data['start_time']
            duration = times_form.cleaned_data['duration']
            stop_time = times_form.cleaned_data['stop_time']
            print(duration)
            x = int(( TotalMinutes(stop_time) - TotalMinutes(start_time) ) / TotalMinutes(duration))

            if saturdays:
                for days in AllSaturdays(length):
                    for i in range(x):
                        total_minutes = TotalMinutes(start_time) + i*TotalMinutes(duration)
                        hours = int(total_minutes/60)
                        minutes = total_minutes - (hours * 60)
                        time = str(hours)+':'+str(minutes)
                        print(minutes)
                        session = SessionModel.objects.create(salon=salon_instance, duration=duration,
                                                    day = str(days), time = time)
                        session.save()
            if sundays:
                for days in AllSundays(length):
                    for i in range(x):
                        total_minutes = TotalMinutes(start_time) + i*TotalMinutes(duration)
                        hours = int(total_minutes/60)
                        minutes = total_minutes - (hours * 60)
                        time = str(hours)+':'+str(minutes)
                        print(minutes)
                        session = SessionModel.objects.create(salon=salon_instance, duration=duration,
                                                    day = str(days), time = time)
                        session.save()
            if saturdays:
                for days in AllSaturdays(length):
                    for i in range(x):
                        total_minutes = TotalMinutes(start_time) + i*TotalMinutes(duration)
                        hours = int(total_minutes/60)
                        minutes = total_minutes - (hours * 60)
                        time = str(hours)+':'+str(minutes)
                        print(minutes)
                        session = SessionModel.objects.create(salon=salon_instance, duration=duration,
                                                    day = str(days), time = time)
                        session.save()
            if mondays:
                for days in AllMondays(length):
                    for i in range(x):
                        total_minutes = TotalMinutes(start_time) + i*TotalMinutes(duration)
                        hours = int(total_minutes/60)
                        minutes = total_minutes - (hours * 60)
                        time = str(hours)+':'+str(minutes)
                        print(minutes)
                        session = SessionModel.objects.create(salon=salon_instance, duration=duration,
                                                    day = str(days), time = time)
                        session.save()


            if tuesdays:
                for days in AllTuesdays(length):
                    for i in range(x):
                        total_minutes = TotalMinutes(start_time) + i*TotalMinutes(duration)
                        hours = int(total_minutes/60)
                        minutes = total_minutes - (hours * 60)
                        time = str(hours)+':'+str(minutes)
                        print(minutes)
                        session = SessionModel.objects.create(salon=salon_instance, duration=duration,
                                                    day = str(days), time = time)
                        session.save()
            if wednesdays:
                for days in AllWednesdays(length):
                    for i in range(x):
                        total_minutes = TotalMinutes(start_time) + i*TotalMinutes(duration)
                        hours = int(total_minutes/60)
                        minutes = total_minutes - (hours * 60)
                        time = str(hours)+':'+str(minutes)
                        print(minutes)
                        session = SessionModel.objects.create(salon=salon_instance, duration=duration,
                                                    day = str(days), time = time)
                        session.save()
            if thursdays:
                for days in AllThursdays(length):
                    for i in range(x):
                        total_minutes = TotalMinutes(start_time) + i*TotalMinutes(duration)
                        hours = int(total_minutes/60)
                        minutes = total_minutes - (hours * 60)
                        time = str(hours)+':'+str(minutes)
                        print(minutes)
                        session = SessionModel.objects.create(salon=salon_instance, duration=duration,
                                                    day = str(days), time = time)
                        session.save()
            if fridays:
                for days in AllFridays(length):
                    for i in range(x):
                        total_minutes = TotalMinutes(start_time) + i*TotalMinutes(duration)
                        hours = int(total_minutes/60)
                        minutes = total_minutes - (hours * 60)
                        time = str(hours)+':'+str(minutes)
                        print(minutes)
                        session = SessionModel.objects.create(salon=salon_instance, duration=duration,
                                                    day = str(days), time = time)
                        session.save()
            return HttpResponseRedirect(reverse('salon:salondetail',
                                                kwargs={'pk':pk}))
    else:
        days_form = DaysForm()
        times_form = TimesForm()
        return render(request,'session/createsession.html',
                              {'days_form':days_form,
                              'times_form':times_form})


@login_required
@sportclub_required
def SessionListView(request,pk):
    salon = get_object_or_404(SalonModel,pk = pk)
    sessions = get_list_or_404(SessionModel.objects.order_by('day'), salon = salon)
    return render(request,'session/sessionlist.html',
                  {'sessions':sessions,
                   'salon':salon})
