from django.shortcuts import render
from django.urls import reverse
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.utils import timezone

#Email send
from django.core.mail import send_mail

#SMS send
from django.utils import timezone
from kavenegar import KavenegarAPI

#handmade
from accounts.forms import UserForm
from accounts.models import UserModel
from accounts.decorators import superuser_required
from masteruser.decorators import masteruser_required
from masteruser.forms import MasterUserForm
from masteruser.models import MasterUserModel
from masteruser.forms import MessageForm, EmailForm

#recaptcha
import json
import urllib
from django.conf import settings
from django.contrib import messages


@superuser_required
def MasterUserSignupView(request):
    registered = False

    if request.method == 'POST':

        user_form = UserForm(data = request.POST)
        masteruser_form = MasterUserForm(data = request.POST)

        if user_form.is_valid() and masteruser_form.is_valid():

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
                     user = user_form.save()
                     user.is_masteruser = True
                     user.save()
                     masteruser = masteruser_form.save(commit=False)
                     masteruser.user = user
                     masteruser.save()
                     registered = True
                     ###
                     superuser_instance = get_object_or_404(UserModel, slug = request.user.slug)
                     superuser_instance_logs = superuser_instance.user_logs

                     new_log = '''
             {previous_logs}\n
             On {date_time}:\n
             Created Masteruser: {user}
             -------------------------------------------------------
                     '''.format(previous_logs = superuser_instance_logs,
                                date_time = timezone.localtime(timezone.now()),
                                 user = str(user.username),)
                     superuser_instance.user_logs = new_log
                     superuser_instance.save()
                     ###
                else:
                     messages.error(request, 'فیلد من ربات نیستم را به درستی کامل کنید')

        else:
            # One of the forms was invalid if this else gets called.
            #redirect to another page or anything else
            print(user_form.errors,masteruser_form.errors)


    else:
        user_form = UserForm()
        masteruser_form = MasterUserForm()

    return render(request,'masteruser/masterusersignup.html',
                          {'user_form':user_form,
                           'masteruser_form':masteruser_form,
                           'registered':registered})


@login_required
@masteruser_required
def MasterUserProfileView(request,slug):
    user_instance = get_object_or_404(UserModel,slug = slug)
    masteruser_instance = get_object_or_404(MasterUserModel, user = user_instance)
    return render(request,'masteruser/masteruserprofile.html',
                  {'masteruser_detail':masteruser_instance})



@method_decorator([login_required, superuser_required], name='dispatch')
class MasterUserListView(ListView):
    model = MasterUserModel
    context_object_name = 'masterusers'
    template_name = 'masteruser/masteruserlist.html'


@method_decorator([login_required, superuser_required], name='dispatch')
class BannedMasterUserListView(ListView):
    model = MasterUserModel
    context_object_name = 'masterusers'
    template_name = 'masteruser/bannedmasteruserlist.html'



@login_required
@superuser_required
def MasterUserBanView(request,slug):
    if request.user.is_superuser:
        user = get_object_or_404(UserModel,slug = slug)
        masteruser = get_object_or_404(MasterUserModel,user = user)
        masteruser.user.is_active = False
        masteruser.user.save()
        superuser_instance = get_object_or_404(UserModel, slug = request.user.slug)
        superuser_instance_logs = superuser_instance.user_logs

        new_log = '''
{previous_logs}\n
On {date_time}:\n
Banned Masteruser: {user}
-------------------------------------------------------
        '''.format(previous_logs = superuser_instance_logs,
                   date_time = timezone.localtime(timezone.now()),
                    user = str(user.username),)
        superuser_instance.user_logs = new_log
        superuser_instance.save()
        return HttpResponseRedirect(reverse('masteruser:detail',
                                            kwargs={'slug':masteruser.user.slug}))
    else:
        return HttpResponseRedirect(reverse('login'))

@login_required
@superuser_required
def MasterUserUnBanView(request,slug):
    if request.user.is_superuser:
        user = get_object_or_404(UserModel,slug = slug)
        masteruser = get_object_or_404(MasterUserModel,user = user)
        masteruser.user.is_active = True
        masteruser.user.save()
        superuser_instance = get_object_or_404(UserModel, slug = request.user.slug)
        superuser_instance_logs = superuser_instance.user_logs

        new_log = '''
{previous_logs}\n
On {date_time}:\n
UnBanned Masteruser: {user}
-------------------------------------------------------
        '''.format(previous_logs = superuser_instance_logs,
                   date_time = timezone.localtime(timezone.now()),
                    user = str(user.username),)
        superuser_instance.user_logs = new_log
        superuser_instance.save()
        return HttpResponseRedirect(reverse('masteruser:detail',
                                            kwargs={'slug':masteruser.user.slug}))
    else:
        return HttpResponseRedirect(reverse('login'))


@login_required
@superuser_required
def MasterUserDeleteView(request,slug):
    if request.user.is_superuser:
        user = get_object_or_404(UserModel,slug = slug)
        masteruser = get_object_or_404(MasterUserModel,user = user)
        masteruser.delete()
        superuser_instance = get_object_or_404(UserModel, slug = request.user.slug)
        superuser_instance_logs = superuser_instance.user_logs

        new_log = '''
{previous_logs}\n
On {date_time}:\n
Deleted Masteruser: {user}
-------------------------------------------------------
        '''.format(previous_logs = superuser_instance_logs,
                   date_time = timezone.localtime(timezone.now()),
                    user = str(user.username),)
        superuser_instance.user_logs = new_log
        superuser_instance.save()
        user.delete()
        return HttpResponseRedirect(reverse('masteruser:bannedlist'))
    else:
        return HttpResponseRedirect(reverse('login'))



@login_required
@superuser_required
def MasterUserDetailView(request,slug):
    if request.user.is_superuser:
        user_instance = get_object_or_404(UserModel, slug = slug)
        masteruser_instance = get_object_or_404(MasterUserModel, user = user_instance)
        return render(request,'masteruser/masteruserdetail.html',
                      {'masteruser':masteruser_instance})
    else:
        return HttpResponseRedirect(reverse('login'))


@login_required
@superuser_required
def MesssageSendingView(request,slug):
    api = KavenegarAPI('30383967456C38706753473546583443536233774E374E6E702B5832386C7648')
    if request.user.is_superuser:
        user_instance = get_object_or_404(UserModel, slug = slug)
        masteruser_instance = get_object_or_404(MasterUserModel, user = user_instance)
        if request.method == 'POST':
            message_form = MessageForm(data = request.POST)
            if message_form.is_valid():
                message_text = message_form.cleaned_data.get('text')
                params = {
                'sender': '100065995',
                'receptor': masteruser_instance.phone_number,
                'message' : message_text
                }
                response = api.sms_send(params)

                superuser_instance = get_object_or_404(UserModel, slug = request.user.slug)
                superuser_instance_logs = superuser_instance.user_logs
                if superuser_instance_logs:
                    new_log = '''
{previous_logs}\n
On {date_time}:\n
SENT A MESSAGE TO: {user} (Master User)\n
Message:\n
{message}
-------------------------------------------------------
                    '''.format(previous_logs = superuser_instance_logs,
                               date_time = timezone.localtime(timezone.now()),
                                user = str(masteruser_instance.user.username),
                                message = str(message_text),)
                else:
                    new_log = '''
On {date_time}:\n
SENT A MESSAGE TO: {user} (Master User)\n
Message:\n
{message}
-------------------------------------------------------
                    '''.format(date_time = timezone.localtime(timezone.now()),
                                user = str(masteruser_instance.user.username),
                                message = str(message_text),)
                superuser_instance.user_logs = new_log
                superuser_instance.save()
                return HttpResponseRedirect(reverse('masteruser:detail',
                                            kwargs={'slug':masteruser_instance.user.slug}))
        else:
            message_form = MessageForm()

            return render(request,'masteruser/messageform.html',
                                  {'form':message_form,})


@login_required
@superuser_required
def EmailSendingView(request,slug):
    if request.user.is_superuser:
        user_instance = get_object_or_404(UserModel, slug = slug)
        masteruser_instance = get_object_or_404(MasterUserModel, user = user_instance)
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
                superuser_instance = get_object_or_404(UserModel, slug = request.user.slug)
                superuser_instance_logs = superuser_instance.user_logs
                if superuser_instance_logs:
                    new_log = '''
{previous_logs}\n
On {date_time}:\n
SENT A MESSAGE TO: {user} (Master User)\n
Email Subject:
{subject}\n
Email Text:\n
{text}
-------------------------------------------------------
                    '''.format(previous_logs = superuser_instance_logs,
                               date_time = timezone.localtime(timezone.now()),
                                user = str(masteruser_instance.user.username),
                                subject = str(email_subject),
                                text = str(email_text),)
                else:
                    new_log = '''
On {date_time}:\n
SENT A MESSAGE TO: {user} (Master User)\n
Email Subject:
{subject}\n
Email Text:\n
{text}
-------------------------------------------------------
                    '''.format(date_time = timezone.localtime(timezone.now()),
                                user = str(masteruser_instance.user.username),
                                subject = str(email_subject),
                                text = str(email_text),)
                superuser_instance.user_logs = new_log
                superuser_instance.save()
                return HttpResponseRedirect(reverse('masteruser:detail',
                                            kwargs={'slug':masteruser_instance.user.slug}))
        else:
            email_form = EmailForm()

            return render(request,'masteruser/emailform.html',
                                  {'form':email_form,})
