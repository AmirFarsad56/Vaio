from sportclub.models import SportClubModel
from django import forms

class SportClubForm(forms.ModelForm):

    class Meta():
        model = SportClubModel
        fields = ('phone_number','address','info','picture')
