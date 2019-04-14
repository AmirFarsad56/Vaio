from django.shortcuts import render
from django.views.generic import DetailView
from django.conf import settings

#handmade
from accounts.models import UserModel
from accoutns.decorators import superuser_required
'''
@superuser_required
class SuperUserProfileView(DetailView):
    model = settings.AUTH_USER_MODEL
    template_name  =
'''
