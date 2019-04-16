from django.shortcuts import render
from django.views.generic import DetailView
from django.conf import settings
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

#handmade
from accounts.models import UserModel
from accounts.decorators import superuser_required


@method_decorator([login_required, superuser_required], name='dispatch')
class SuperUserProfileView(DetailView):
    model = UserModel
    context_object_name = 'superuser'
    template_name = 'accounts/superuserprofile.html'

    def get_queryset(self):
        return UserModel.objects.filter(username = self.request.user.username )
