from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import UpdateView, DeleteView, DetailView, ListView
from django.forms import modelformset_factory
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

#handmade
from accounts.models import UserModel
from sportclub.models import SportClubModel
from salon.forms import SalonForm, SalonPictureForm
from salon.models import SalonModel, SalonPictureModel
from sportclub.decorators import sportclub_required
from accounts.decorators import superuser_required
from masteruser.decorators import masteruser_required


#recaptcha
import json
import urllib
from django.conf import settings
from django.contrib import messages




@login_required
@sportclub_required
def SalonCreateView(request,slug):
    user = get_object_or_404(UserModel, slug=slug)
    sportclub = get_object_or_404(SportClubModel, user = user)
    if sportclub == request.user.sportclubs:

        imageformset = modelformset_factory(SalonPictureModel,
                                            form=SalonPictureForm, extra=4)
        pending = True
        if request.method == 'POST':
            salon_form = SalonForm(data = request.POST)
            formsets = imageformset(request.POST or None, request.FILES or None)
            if salon_form.is_valid() and formsets.is_valid():

                messages.success(request,'سالن با موفقیت اضافه شد')
                salon = salon_form.save(commit=False)
                #sportclub = get_object_or_404(SportClubModel, slug=slug)
                salon.sportclub = sportclub
                salon.save()
                pending = False
                for formset in formsets.cleaned_data:
                    if formset:
                        picture = formset['picture']
                        photo = SalonPictureModel(salon = salon, picture = picture)
                        photo.save()
            else:
                print(salon_form.errors)
        else:
            salon_form = SalonForm()
            formsets = imageformset(queryset=SalonPictureModel.objects.none())
    else:
        return HttpResponseRedirect(reverse('login'))
    return render(request,'salon/createsalon.html',
                  {'salon_form':salon_form,
                  'formsets':formsets,
                   'pending':pending})


@method_decorator([login_required, sportclub_required], name='dispatch')
class SalonUpdateView(UpdateView):
    model = SalonModel
    fields = '__all__'
    template_name = 'salon/updatesalon.html'

    def get_queryset(self):
        return SalonModel.objects.filter(sportclub = self.request.user.sportclubs)



@method_decorator([login_required, sportclub_required], name='dispatch')
class SalonDetailView(DetailView):
    model = SalonModel
    context_object_name = 'salon_detail'
    template_name = 'salon/salondetail.html'

    def get_queryset(self):
        return SalonModel.objects.filter(sportclub = self.request.user.sportclubs)


@method_decorator([login_required, masteruser_required], name='dispatch')
class PublishedSalonListView(ListView):
    model = SalonModel
    context_object_name = 'salons'
    template_name = 'salon/publishedsalonlist.html'


@method_decorator([login_required, masteruser_required], name='dispatch')
class UnPublishedSalonListView(ListView):
    model = SalonModel
    context_object_name = 'salons'
    template_name = 'salon/unpublishedsalonlist.html'


@login_required
@masteruser_required
def SalonConfirmView(request,pk):
    if request.user.is_masteruser:
        salon = get_object_or_404(SalonModel,pk = pk)
        if request.method == 'POST':

            salon.confirm()
            return HttpResponseRedirect(reverse('salon:unpublishedsalonlist'))
        else:
            return render(request,'salon/salonconfirm.html',
                          {'salon_detail':salon})
    else:
        return HttpResponseRedirect(reverse('login'))
'''
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

'''
