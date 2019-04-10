from django import forms
from salon.models import SalonModel, SalonPictureModel

class SalonForm(forms.ModelForm):

    class Meta():
        model = SalonModel
        fields = ('area','floor_type','locker',
                  'drinking_water','parking_area','shower',
                  'changing_room')

class SalonPictureForm(forms.ModelForm):

    class Meta():
        model = SalonPictureModel
        fields = ('picture',)
