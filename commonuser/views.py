
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


#handmade classes
from commonuser.forms import CommonUserForm
from accounts.forms import UserForm
from commonuser.models import CommonUserModel
from accounts.models import UserModel
from masteruser.decorators import masteruser_required

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


class CommonUserProfileView(DetailView):
    model = CommonUserModel
    context_object_name = 'commonuser_detail'
    template_name = 'commonuser/commonuserprofile.html'


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
        #later set sessions is_booked = False here
        ############################## change this to commonuser detail page
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
        ############################## change this to commonuser detail page
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
        user_instance.delete()
        return HttpResponseRedirect(reverse('commonuser:bannedlist'))
    else:
        return HttpResponseRedirect(reverse('login'))


@method_decorator([login_required, masteruser_required], name='dispatch')
class BannedCommonUserListView(ListView):
    model = CommonUserModel
    context_object_name = 'commonusers'
    template_name = 'commonuser/bannedcommonuserlist.html'
