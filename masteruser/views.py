from django.shortcuts import render
from django.urls import reverse
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


#handmade
from accounts.forms import UserForm
from accounts.decorators import superuser_required
from masteruser.forms import MasterUserForm
from masteruser.models import MasterUserModel

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
                     user.slug = slugify(user.username)
                     user.save()
                     masteruser = masteruser_form.save(commit=False)
                     masteruser.user = user
                     masteruser.save()
                     registered = True
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

@method_decorator([login_required, superuser_required], name='dispatch')
class MasterUserListView(ListView):
    model = MasterUserModel
    context_object_name = 'masterusers'
    template_name = 'masteruser/masteruserlist.html'

@login_required
@superuser_required
def MasterUserBanView(request,pk):
    if request.user.is_superuser:
        masteruser = get_object_or_404(MasterUserModel,pk = pk)
        if request.method == 'POST':
            masteruser.user.is_active = False
            masteruser.user.save()
            return HttpResponseRedirect(reverse('masteruser:list'))
        else:
            return render(request,'masteruser/masteruserban.html',
                          {'masteruser':masteruser})
    else:
        return HttpResponseRedirect(reverse('login'))

@login_required
@superuser_required
def MasterUserUnBanView(request,pk):
    if request.user.is_superuser:
        masteruser = get_object_or_404(MasterUserModel,pk = pk)
        if request.method == 'POST':
            masteruser.user.is_active = True
            masteruser.user.save()
            return HttpResponseRedirect(reverse('masteruser:list'))
        else:
            return render(request,'masteruser/masteruserunban.html',
                          {'masteruser':masteruser})
    else:
        return HttpResponseRedirect(reverse('login'))


@login_required
@superuser_required
def MasterUserDeleteView(request,pk):
    if request.user.is_superuser:
        masteruser = get_object_or_404(MasterUserModel,pk = pk)
        submited = False
        if request.method == 'POST':
            masteruser.delete()
            masteruser.user.delete()
            return HttpResponseRedirect(reverse('masteruser:list'))
        else:
            return render(request,'masteruser/masteruserdelete.html',
                          {'masteruser':masteruser})
    else:
        return HttpResponseRedirect(reverse('login'))
