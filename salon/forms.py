from django import forms
from salon.models import SalonModel

class SalonForm(forms.ModelForm):

    class Meta():
        model = SalonModel
        fields = ('area','floor_type','locker',
                  'drinking_water','parking_area','showers',
                  'changing_room','picture')
