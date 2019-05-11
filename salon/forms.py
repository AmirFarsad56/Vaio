from django import forms
from salon.models import SalonModel, SalonPictureModel

class SalonForm(forms.ModelForm):

    class Meta():
        model = SalonModel
        fields = ('area','floor_type','locker',
                  'drinking_water','parking_area','shower',
                  'changing_room','is_futsall','is_volleyball',
                  'is_football','is_basketball','safe_keeping')

class SalonPictureForm(forms.ModelForm):

    class Meta():
        model = SalonPictureModel
        fields = ('picture',)


class SalonConfirmForm(forms.ModelForm):

    class Meta():
        model = SalonModel
        fields = ('is_confirmed',)
