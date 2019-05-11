from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.utils import timezone

#SMS send
from django.utils import timezone
from kavenegar import KavenegarAPI

#handmade classes
from commonuser.forms import CommonUserForm, CommonUserUpdateForm
from accounts.forms import UserForm, UserUpdateForm
from commonuser.models import CommonUserModel
from accounts.models import UserModel
from masteruser.decorators import masteruser_required
from commonuser.forms import MessageForm, EmailForm

#recaptcha
import json
import urllib
from django.conf import settings
from django.contrib import messages


def CommonUserSignupView(request):
    registered = False

    if request.method == 'POST':

        user_form = UserForm(data = request.POST)
        commonuser_form = CommonUserForm(data = request.POST)

        if user_form.is_valid() and commonuser_form.is_valid():

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
                     user = user_form.save(commit=False)
                     user.is_commonuser = True
                     user.save()
                     commonuser = commonuser_form.save(commit=False)
                     commonuser.user = user
                     if 'picture' in request.FILES:
                        commonuser.picture = request.FILES['picture']

                     commonuser.save()
                     registered = True
                else:
                     messages.error(request, 'فیلد من ربات نیستم را به درستی کامل کنید')

        else:
            # One of the forms was invalid if this else gets called.
            #redirect to another page or anything else
            print(user_form.errors,commonuser_form.errors)


    else:
        user_form = UserForm()
        commonuser_form = CommonUserForm()

    return render(request,'commonuser/commonusersignup.html',
                          {'user_form':user_form,
                           'commonuser_form':commonuser_form,
                           'registered':registered})


@login_required
def CommonUserProfileView(request,slug):
    user_instance = get_object_or_404(UserModel,slug = slug)
    commonuser_instance = get_object_or_404(CommonUserModel, user = user_instance)
    return render(request,'commonuser/commonuserprofile.html',
                  {'commonuser_detail':commonuser_instance})


@method_decorator([login_required, masteruser_required], name='dispatch')
class CommonUserListView(ListView):
    model = CommonUserModel
    context_object_name = 'commonusers'
    template_name = 'commonuser/commonuserlist.html'


@login_required
@masteruser_required
def CommonUserDetailView(request,slug):
    if request.user.is_masteruser:
        user_instance = get_object_or_404(UserModel, slug = slug)
        commonuser_instance = get_object_or_404(CommonUserModel, user = user_instance)
        #later add booked_sessions to DetailView
        return render(request,'commonuser/commonuserdetail.html',
                      {'commonuser_detail':commonuser_instance})
    else:
        return HttpResponseRedirect(reverse('login'))


@login_required
@masteruser_required
def CommonUserBanView(request,slug):
    if request.user.is_masteruser:
        user_instance = get_object_or_404(UserModel, slug = slug)
        user_instance.is_active = False
        user_instance.save()
        #later set related sessions is_booked = False here
        ############################## change this to commonuser detail page
        masteruser_instance = get_object_or_404(UserModel, slug = request.user.slug)
        masteruser_instance_logs = masteruser_instance.user_logs

        new_log = '''{previous_logs}\n
On {date_time}:\n
Banned CommonUser: {user}
-------------------------------------------------------
        '''.format(previous_logs = masteruser_instance_logs,
                   date_time = timezone.localtime(timezone.now()),
                    user = str(user_instance.username),)
        masteruser_instance.user_logs = new_log
        masteruser_instance.save()
        ########################################
        return HttpResponseRedirect(reverse("commonuser:detail",
                                            kwargs={'slug':user_instance.slug}))
    else:
        return HttpResponseRedirect(reverse('login'))


@login_required
@masteruser_required
def CommonUserUnBanView(request,slug):
    if request.user.is_masteruser:
        user_instance = get_object_or_404(UserModel, slug = slug)
        user_instance.is_active = True
        user_instance.save()
        masteruser_instance = get_object_or_404(UserModel, slug = request.user.slug)
        masteruser_instance_logs = masteruser_instance.user_logs

        new_log = '''{previous_logs}\n
On {date_time}:\n
UnBanned CommonUser: {user}
-------------------------------------------------------
        '''.format(previous_logs = masteruser_instance_logs,
                   date_time = timezone.localtime(timezone.now()),
                    user = str(user_instance.username),)
        masteruser_instance.user_logs = new_log
        masteruser_instance.save()
        return HttpResponseRedirect(reverse("commonuser:detail",
                                            kwargs={'slug':user_instance.slug}))
    else:
        return HttpResponseRedirect(reverse('login'))


@login_required
@masteruser_required
def CommonUserDeleteView(request,slug):
    if request.user.is_masteruser:
        user_instance = get_object_or_404(UserModel, slug = slug)
        commonuser_instance = get_object_or_404(CommonUserModel, user = user_instance)
        commonuser_instance.delete()
        masteruser_instance = get_object_or_404(UserModel, slug = request.user.slug)
        masteruser_instance_logs = masteruser_instance.user_logs

        new_log = '''{previous_logs}\n
On {date_time}:\n
Deleted CommonUser: {user}
-------------------------------------------------------
        '''.format(previous_logs = masteruser_instance_logs,
                   date_time = timezone.localtime(timezone.now()),
                    user = str(user_instance.username),)
        masteruser_instance.user_logs = new_log
        masteruser_instance.save()
        user_instance.delete()
        return HttpResponseRedirect(reverse('commonuser:bannedlist'))
    else:
        return HttpResponseRedirect(reverse('login'))


@method_decorator([login_required, masteruser_required], name='dispatch')
class BannedCommonUserListView(ListView):
    model = CommonUserModel
    context_object_name = 'commonusers'
    template_name = 'commonuser/bannedcommonuserlist.html'



@login_required
@masteruser_required
def MesssageSendingView(request,slug):
    api = KavenegarAPI('30383967456C38706753473546583443536233774E374E6E702B5832386C7648')
    if request.user.is_masteruser:
        user_instance = get_object_or_404(UserModel, slug = slug)
        commonuser_instance = get_object_or_404(CommonUserModel, user = user_instance)
        if request.method == 'POST':
            message_form = MessageForm(data = request.POST)
            if message_form.is_valid():
                message_text = message_form.cleaned_data.get('text')
                params = {
                'sender': '100065995',
                'receptor': commonuser_instance.phone_number,
                'message' : message_text
                }
                response = api.sms_send(params)

                masteruser_instance = get_object_or_404(UserModel, slug = request.user.slug)
                masteruser_instance_logs = masteruser_instance.user_logs
                new_log = '''{previous_logs}\n
On {date_time}:\n
Sent a message to: {user} (Common User)\n
Message:\n
{message}
-------------------------------------------------------
                '''.format(previous_logs = masteruser_instance_logs,
                           date_time = timezone.localtime(timezone.now()),
                            user = str(commonuser_instance.user.username),
                            message = str(message_text),)

                masteruser_instance.user_logs = new_log
                masteruser_instance.save()
                return HttpResponseRedirect(reverse('commonuser:detail',
                                            kwargs={'slug':commonuser_instance.user.slug}))
        else:
            message_form = MessageForm()

            return render(request,'commonuser/messageform.html',
                                  {'form':message_form,})


@login_required
@masteruser_required
def EmailSendingView(request,slug):
    if request.user.is_masteruser:
        user_instance = get_object_or_404(UserModel, slug = slug)
        commonuser_instance = get_object_or_404(CommonUserModel, user = user_instance)
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
                new_log = '''{previous_logs}\n
On {date_time}:\n
Sent an Email to: {user} (Common User)\n
Email Subject:
{subject}\n
Email Text:\n
{text}
-------------------------------------------------------
                '''.format(previous_logs = masteruser_instance_logs,
                           date_time = timezone.localtime(timezone.now()),
                            user = str(commonuser_instance.user.username),
                            subject = str(email_subject),
                            text = str(email_text),)
                masteruser_instance.user_logs = new_log
                masteruser_instance.save()
                return HttpResponseRedirect(reverse('commonuser:detail',
                                            kwargs={'slug':commonuser_instance.user.slug}))
        else:
            email_form = EmailForm()

            return render(request,'commonuser/emailform.html',
                                  {'form':email_form,})


@login_required
def CommonUserUpdateView(request,slug):
    commonuser_user = get_object_or_404(UserModel,slug = slug)
    user_update_form = UserUpdateForm(request.POST or None, instance = commonuser_user)
    commonuser = get_object_or_404(CommonUserModel, user = commonuser_user)
    commonuser_update_form = CommonUserUpdateForm(request.POST or None, instance = commonuser)
    if commonuser_update_form.is_valid() and user_update_form.is_valid():
        user_update_form.save()
        commonuser_update_form.save()
        if 'picture' in request.FILES:
           commonuser.picture = request.FILES['picture']
           commonuser.save()
        return HttpResponseRedirect(reverse('commonuser:profile',
                                    kwargs={'slug':commonuser_user.slug}))
    return render(request,'commonuser/commonuserupdate.html',
                          {'commonuserform':commonuser_update_form,
                           'userform':user_update_form,})
