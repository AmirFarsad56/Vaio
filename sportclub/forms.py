from sportclub.models import SportClubModel
from django import forms

class SportClubForm(forms.ModelForm):

    class Meta():
        model = SportClubModel
        fields = ('phone_number','address','info','picture')


class MessageForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)


class EmailForm(forms.Form):
    subject = forms.CharField(widget=forms.Textarea)
    text = forms.CharField(widget=forms.Textarea)
