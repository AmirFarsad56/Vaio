from django.shortcuts import render
from django.views.generic import DetailView, UpdateView
from django.conf import settings
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

#handmade
from accounts.models import UserModel
from accounts.decorators import superuser_required
from accounts.forms import EmailForm, MessageForm, TypesForm
from commonuser.models import CommonUserModel
from sportclub.models import SportClubModel
from masteruser.models import MasterUserModel

#Email send
from django.core.mail import send_mail

#SMS send
from django.utils import timezone
from kavenegar import KavenegarAPI


@method_decorator([login_required, superuser_required], name='dispatch')
class SuperUserProfileView(DetailView):
    model = UserModel
    context_object_name = 'superuser'
    template_name = 'accounts/superuserprofile.html'

    def get_queryset(self):
        return UserModel.objects.filter(username = self.request.user.username )


@method_decorator([login_required, superuser_required], name='dispatch')
class SuperUserUpdateView(UpdateView):
    model = UserModel
    fields = ('first_name','last_name','picture','email')
    template_name = 'accounts/superuserupdate.html'

    def get_queryset(self):
        return UserModel.objects.filter(username = self.request.user.username )

    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse("accounts:profile", kwargs={'slug': slug})


@login_required
@superuser_required
def CloudMessageView(request):
    api = KavenegarAPI('30383967456C38706753473546583443536233774E374E6E702B5832386C7648')
    if request.user.is_superuser:

        if request.method == 'POST':
            types_form = TypesForm(data = request.POST )
            message_form = MessageForm(data = request.POST)
            if message_form.is_valid() and types_form.is_valid():
                masterusers = types_form.cleaned_data['masterusers']
                sportclubs = types_form.cleaned_data['sportclubs']
                commonusers = types_form.cleaned_data['commonusers']
                message_text = message_form.cleaned_data.get('text')

                if masterusers:
                    master_users = MasterUserModel.objects.all()
                    for master_user in master_users:
                        params = {
                        'sender': '100065995',
                        'receptor': master_user.phone_number,
                        'message' : message_text
                        }
                        response = api.sms_send(params)
                if sportclubs:
                    sport_clubs = SportClubModel.objects.all()
                    for sport_club in sport_clubs:
                        params = {
                        'sender': '100065995',
                        'receptor': sport_club.phone_number,
                        'message' : message_text
                        }
                        response = api.sms_send(params)
                if commonusers:
                    common_users = CommonUserModel.objects.all()
                    for common_user in common_users:
                        params = {
                        'sender': '100065995',
                        'receptor': common_user.phone_number,
                        'message' : message_text
                        }
                        response = api.sms_send(params)


                superuser_instance = get_object_or_404(UserModel, slug = request.user.slug)
                superuser_instance_logs = superuser_instance.user_logs
                to = ''
                if commonusers:
                    to += 'Common Users '
                if sportclubs:
                    to += 'Sport Clubs '
                if masterusers:
                    to += 'Master Users '
                new_log = '''
{previous_logs}\n
On {date_time}:\n
Sent Cloud Message To: {to}\n
Message:\n
{message}
-------------------------------------------------------
                '''.format(previous_logs = superuser_instance_logs,
                           date_time = timezone.localtime(timezone.now()),
                            to = to,
                            message = str(message_text),)
                superuser_instance.user_logs = new_log
                superuser_instance.save()
                return HttpResponseRedirect(reverse('accounts:profile',
                                            kwargs={'slug':request.user.slug}))
        else:
            message_form = MessageForm()
            types_form = TypesForm()

            return render(request,'accounts/cloudmessage.html',
                                  {'message_form':message_form,
                                   'types_form':types_form})


@login_required
@superuser_required
def CloudEmailView(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            email_form = EmailForm(data = request.POST)
            types_form = userlist = TypesForm(data = request.POST)
            if email_form.is_valid() and types_form.is_valid():
                users = UserModel.objects.all()
                email_subject = email_form.cleaned_data.get('subject')
                email_text = email_form.cleaned_data.get('text')
                masterusers = types_form.cleaned_data['masterusers']
                sportclubs = types_form.cleaned_data['sportclubs']
                commonusers = types_form.cleaned_data['commonusers']
                for user in users:
                    if masterusers and user.is_masteruser :
                        send_mail(
                        email_subject,
                        email_text,
                        'alienone306@gmail.com',
                        [user.email,],
                        fail_silently=False,
                        )
                    if sportclubs and user.is_sportclub :
                        send_mail(
                        email_subject,
                        email_text,
                        'alienone306@gmail.com',
                        [user.email,],
                        fail_silently=False,
                        )
                    if commonusers and user.is_commonuser :
                        send_mail(
                        email_subject,
                        email_text,
                        'alienone306@gmail.com',
                        [user.email,],
                        fail_silently=False,
                        )


                superuser_instance = get_object_or_404(UserModel, slug = request.user.slug)
                superuser_instance_logs = superuser_instance.user_logs
                to = ''
                if commonusers:
                    to += 'Common Users '
                if sportclubs:
                    to += 'Sport Clubs '
                if masterusers:
                    to += 'Master Users '
                new_log = '''
{previous_logs}\n
On {date_time}:\n
Sent Cloud Email To: {to}\n
Email Subject:
{subject}\n
Email Text:\n
{text}
-------------------------------------------------------
                '''.format(previous_logs = superuser_instance_logs,
                           date_time = timezone.localtime(timezone.now()),
                            to = to,
                            subject = str(email_subject),
                            text = str(email_text),)
                superuser_instance.user_logs = new_log
                superuser_instance.save()
                return HttpResponseRedirect(reverse('accounts:profile',
                                            kwargs={'slug':request.user.slug}))
        else:
            email_form = EmailForm()
            types_form = TypesForm()

            return render(request,'accounts/cloudemail.html',
                                  {'email_form':email_form,
                                   'types_form':types_form})
