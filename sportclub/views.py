from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.text import slugify
from django.shortcuts import get_object_or_404, get_list_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.utils import timezone

#SMS send
from django.utils import timezone
from kavenegar import KavenegarAPI

#handmade classes
from accounts.models import UserModel
from sportclub.forms import SportClubForm
from accounts.forms import UserForm
from sportclub.models import SportClubModel
from accounts.models import UserModel
from salon.models import SalonModel
from sportclub.decorators import sportclub_required
from masteruser.decorators import masteruser_required
from sportclub.forms import MessageForm, EmailForm


#recaptcha
import json
import urllib
from django.conf import settings
from django.contrib import messages

@masteruser_required
def SportClubSignupView(request):
    registered = False

    if request.method == 'POST':

        user_form = UserForm(data = request.POST)
        sportclub_form = SportClubForm(data = request.POST)

        if user_form.is_valid() and sportclub_form.is_valid():

                recaptcha_response = request.POST.get('g-recaptcha-response')
                url = 'https://www.google.com/recaptcha/api/siteverify'
                values = {
                    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                    'response': recaptcha_response
                }
                data = urllib.parse.urlencode(values).encode()
                req =  urllib.request.Request(url, data=data)
                response = urllib.request.urlopen(req)
                result = json.loads(response.read().decode())
                ''' End reCAPTCHA validation '''
                if result['success']:
                     messages.success(request, 'ثبت نام با موفقیت انجام شد')
                     user = user_form.save(commit = False)#changed this if sth wrong happen ..
                     user.is_sportclub = True
                     user.save()
                     sportclub = sportclub_form.save(commit=False)
                     sportclub.user = user
                     if 'picture' in request.FILES:
                        sportclub.picture = request.FILES['picture']

                     sportclub.save()
                     registered = True
                     masteruser_instance = get_object_or_404(UserModel, slug = request.user.slug)
                     masteruser_instance_logs = masteruser_instance.user_logs

                     new_log = '''
 {previous_logs}\n
 On {date_time}:\n
 Created a new SportClub: {sportclub}
 -------------------------------------------------------
                     '''.format(previous_logs = masteruser_instance_logs,
                                date_time = timezone.localtime(timezone.now()),
                                 sportclub = str(user.username),)
                     masteruser_instance.user_logs = new_log
                     masteruser_instance.save()
                else:
                     messages.error(request, 'فیلد من ربات نیستم را به درستی کامل کنید')

        else:
            # One of the forms was invalid if this else gets called.
            #redirect to another page or anything else
            print(user_form.errors,sportclub_form.errors)


    else:
        user_form = UserForm()
        sportclub_form = SportClubForm()

    return render(request,'sportclub/sportclubsignup.html',
                          {'user_form':user_form,
                           'sportclub_form':sportclub_form,
                           'registered':registered})


@sportclub_required
@login_required
def SportClubProfileView(request, slug):
    user = request.user
    SportClubDetail = get_object_or_404(SportClubModel, user = user)
    return render(request,'sportclub/sportclubprofile.html',
                    {'sportclub_detail':SportClubDetail})


@method_decorator([login_required, masteruser_required], name='dispatch')
class SportClubListView(ListView):
    model = SportClubModel
    context_object_name = 'sportclubs'
    template_name = 'sportclub/sportclublist.html'


@login_required
@masteruser_required
def SportClubDetailView(request,slug):
    if request.user.is_masteruser:
        user_instance = get_object_or_404(UserModel, slug = slug)
        sportclub_instance = get_object_or_404(SportClubModel, user = user_instance)

        try:
            salon_instances = get_list_or_404(SalonModel, sportclub = sportclub_instance)
            return render(request,'sportclub/sportclubdetail.html',
                          {'sportclub_detail':sportclub_instance,
                           'salons':salon_instances})
        except:
            return render(request,'sportclub/sportclubdetail.html',
                          {'sportclub_detail':sportclub_instance})
    else:
        return HttpResponseRedirect(reverse('login'))


@login_required
@masteruser_required
def BannedSportClubExceptionView(request,slug):
    if request.user.is_masteruser:
        user_instance = get_object_or_404(UserModel, slug = slug)
        sportclub_instance = get_object_or_404(SportClubModel, user = user_instance)
        salon_instances = get_list_or_404(SalonModel, sportclub = sportclub_instance)
        return render(request,'sportclub/bannedsportclubexception.html',
                      {'sportclub_detail':sportclub_instance,
                       'salons':salon_instances})
    else:
        return HttpResponseRedirect(reverse('login'))


@login_required
@masteruser_required
def SportClubBanView(request,slug):
    if request.user.is_masteruser:
        user_instance = get_object_or_404(UserModel, slug = slug)
        user_instance.is_active = False
        user_instance.save()
        sportclub_instance = get_object_or_404(SportClubModel, user = user_instance)
        salon_instances = get_list_or_404(SalonModel, sportclub = sportclub_instance)
        for salon_instance in salon_instances:
            salon_instance.is_confirmed = False
            salon_instance.save()
        masteruser_instance = get_object_or_404(UserModel, slug = request.user.slug)
        masteruser_instance_logs = masteruser_instance.user_logs

        new_log = '''
{previous_logs}\n
On {date_time}:\n
Banned Sportclub: {user}
-------------------------------------------------------
        '''.format(previous_logs = masteruser_instance_logs,
                   date_time = timezone.localtime(timezone.now()),
                    user = str(user_instance.username),)
        masteruser_instance.user_logs = new_log
        masteruser_instance.save()
        return HttpResponseRedirect(reverse("sportclub:detail",
                                            kwargs={'slug':user_instance.slug}))
    else:
        return HttpResponseRedirect(reverse('login'))


@login_required
@masteruser_required
def SportClubUnBanView(request,slug):
    if request.user.is_masteruser:
        user_instance = get_object_or_404(UserModel, slug = slug)
        user_instance.is_active = True
        user_instance.save()
        masteruser_instance = get_object_or_404(UserModel, slug = request.user.slug)
        masteruser_instance_logs = masteruser_instance.user_logs

        new_log = '''
{previous_logs}\n
On {date_time}:\n
UnBanned Sportclub: {user}
-------------------------------------------------------
        '''.format(previous_logs = masteruser_instance_logs,
                   date_time = timezone.localtime(timezone.now()),
                    user = str(user_instance.username),)
        masteruser_instance.user_logs = new_log
        masteruser_instance.save()
        return HttpResponseRedirect(reverse("sportclub:detail",
                                            kwargs={'slug':user_instance.slug}))
    else:
        return HttpResponseRedirect(reverse('login'))



@login_required
@masteruser_required
def SportClubDeleteView(request,slug):
    if request.user.is_masteruser:
        user_instance = get_object_or_404(UserModel, slug = slug)
        sportclub_instance = get_object_or_404(SportClubModel, user = user_instance)
        sportclub_instance.delete()
        masteruser_instance = get_object_or_404(UserModel, slug = request.user.slug)
        masteruser_instance_logs = masteruser_instance.user_logs

        new_log = '''
{previous_logs}\n
On {date_time}:\n
Deleted Sportclub: {user}
-------------------------------------------------------
        '''.format(previous_logs = masteruser_instance_logs,
                   date_time = timezone.localtime(timezone.now()),
                    user = str(user_instance.username),)
        masteruser_instance.user_logs = new_log
        masteruser_instance.save()
        user_instance.delete()

        return HttpResponseRedirect(reverse('sportclub:bannedlist'))
    else:
        return HttpResponseRedirect(reverse('login'))


@method_decorator([login_required, masteruser_required], name='dispatch')
class BannedSportClubListView(ListView):
    model = SportClubModel
    context_object_name = 'sportclubs'
    template_name = 'sportclub/bannedsportclublist.html'


@login_required
@masteruser_required
def MesssageSendingView(request,slug):
    api = KavenegarAPI('30383967456C38706753473546583443536233774E374E6E702B5832386C7648')
    if request.user.is_masteruser:
        user_instance = get_object_or_404(UserModel, slug = slug)
        sportclub_instance = get_object_or_404(SportClubModel, user = user_instance)
        if request.method == 'POST':
            message_form = MessageForm(data = request.POST)
            if message_form.is_valid():
                message_text = message_form.cleaned_data.get('text')
                params = {
                'sender': '100065995',
                'receptor': sportclub_instance.phone_number,
                'message' : message_text
                }
                response = api.sms_send(params)

                masteruser_instance = get_object_or_404(UserModel, slug = request.user.slug)
                masteruser_instance_logs = masteruser_instance.user_logs
                if masteruser_instance_logs:
                    new_log = '''
{previous_logs}\n
On {date_time}:\n
SENT A MESSAGE TO: {user} (Sport Club)\n
Message:\n
{message}
-------------------------------------------------------
                    '''.format(previous_logs = masteruser_instance_logs,
                               date_time = timezone.localtime(timezone.now()),
                                user = str(sportclub_instance.user.username),
                                message = str(message_text),)
                else:
                    new_log = '''
On {date_time}:\n
SENT A MESSAGE TO: {user} (Sport Club)\n
Message:\n
{message}
-------------------------------------------------------
                    '''.format(date_time = timezone.localtime(timezone.now()),
                                user = str(sportclub_instance.user.username),
                                message = str(message_text),)
                masteruser_instance.user_logs = new_log
                masteruser_instance.save()
                return HttpResponseRedirect(reverse('sportclub:detail',
                                            kwargs={'slug':sportclub_instance.user.slug}))
        else:
            message_form = MessageForm()

            return render(request,'sportclub/messageform.html',
                                  {'form':message_form,})


@login_required
@masteruser_required
def EmailSendingView(request,slug):
    if request.user.is_masteruser:
        user_instance = get_object_or_404(UserModel, slug = slug)
        sportclub_instance = get_object_or_404(SportClubModel, user = user_instance)
        if request.method == 'POST':
            email_form = EmailForm(data = request.POST)
            if email_form.is_valid():
                email_subject = email_form.cleaned_data.get('subject')
                email_text = email_form.cleaned_data.get('text')
                send_mail(
                email_subject,
                email_text,
                'alienone306@gmail.com',
                [user_instance.email,],
                fail_silently=False,
                )
                masteruser_instance = get_object_or_404(UserModel, slug = request.user.slug)
                masteruser_instance_logs = masteruser_instance.user_logs
                if masteruser_instance_logs:
                    new_log = '''
{previous_logs}\n
On {date_time}:\n
SENT AN EMAIL TO: {user} (Sport Club)\n
Email Subject:
{subject}\n
Email Text:\n
{text}
-------------------------------------------------------
                    '''.format(previous_logs = masteruser_instance_logs,
                               date_time = timezone.localtime(timezone.now()),
                                user = str(sportclub_instance.user.username),
                                subject = str(email_subject),
                                text = str(email_text),)
                else:
                    new_log = '''
On {date_time}:\n
SENT A MESSAGE TO: {user} (Sport Club)\n
Email Subject:
{subject}\n
Email Text:\n
{text}
-------------------------------------------------------
                    '''.format(date_time = timezone.localtime(timezone.now()),
                                user = str(sportclub_instance.user.username),
                                subject = str(email_subject),
                                text = str(email_text),)
                masteruser_instance.user_logs = new_log
                masteruser_instance.save()
                return HttpResponseRedirect(reverse('sportclub:detail',
                                            kwargs={'slug':sportclub_instance.user.slug}))
        else:
            email_form = EmailForm()

            return render(request,'sportclub/emailform.html',
                                  {'form':email_form,})
