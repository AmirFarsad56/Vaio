from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import UpdateView, DeleteView, DetailView
from django.forms import modelformset_factory
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

#handmade
from sportclub.models import SportClubModel
from salon.forms import SalonForm, SalonPictureForm
from salon.models import SalonModel, SalonPictureModel
from sportclub.decorators import sportclub_required


#recaptcha
import json
import urllib
from django.conf import settings
from django.contrib import messages





def SalonCreateView(request,slug):
    imageformset = modelformset_factory(SalonPictureModel,
                                        form=SalonPictureForm, extra=4)
    pending = True
    if request.method == 'POST':
        salon_form = SalonForm(data = request.POST)
        formsets = imageformset(request.POST or None, request.FILES or None)
        if salon_form.is_valid() and formsets.is_valid():

            messages.success(request,'سالن با موفقیت اضافه شد')
            salon = salon_form.save(commit=False)
            sportclub = get_object_or_404(SportClubModel, slug=slug)
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

    return render(request,'salon/createsalon.html',
                  {'salon_form':salon_form,
                  'formsets':formsets,
                   'pending':pending})

class SalonUpdateView(UpdateView):
    model = SalonModel
    fields = '__all__'
    template_name = 'salon/updatesalon.html'

@method_decorator([login_required, sportclub_required], name='dispatch')
class SalonDetailView(DetailView):
    model = SalonModel
    context_object_name = 'salon_detail'
    template_name = 'salon/salondetail.html'
    def get_queryset(self):
        return SalonModel.objects.filter(sportclub = self.request.user.sportclubs)
