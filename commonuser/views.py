
from django.shortcuts import render, redirect
from django.views.generic import ListView
from commonuser.forms import CommonUserForm
from accounts.forms import UserForm
from commonuser.models import CommonUserModel
from accounts.models import UserModel

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
                     user = user_form.save()
                     #user.set_password(user.password)
                     user.is_commonuser = True
                     user.save()
                     commonuser = commonuser_form.save(commit=False)
                     commonuser.user = user
                     #not dealing well with picture
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

class CommonUserListView(ListView):
    template_name = 'commonuser/commonuserlist.html'
    context_object_name = 'users'
    model = UserModel

