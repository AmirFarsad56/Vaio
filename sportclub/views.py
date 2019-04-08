from django.shortcuts import render, redirect
from django.views.generic import DetailView

#handmade classes
from sportclub.forms import SportClubForm
from accounts.forms import UserForm
from sportclub.models import SportClubModel
from accounts.models import UserModel


#recaptcha
import json
import urllib
from django.conf import settings
from django.contrib import messages


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
                     user = user_form.save()
                     #user.set_password(user.password)
                     user.is_sportclub = True
                     user.save()
                     sportclub = sportclub_form.save(commit=False)
                     sportclub.user = user
                     #not dealing well with picture
                     if 'picture' in request.FILES:
                        sportclub.picture = request.FILES['picture']

                     sportclub.save()
                     registered = True
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


class SportClubProfileView(DetailView):
    model = SportClubModel
    context_object_name = 'sportclub_detail'
    template_name = 'sportclub/sportclubprofile.html'
