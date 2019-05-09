from django import forms
from masteruser.models import MasterUserModel


class MasterUserForm(forms.ModelForm):

    class Meta:
        model = MasterUserModel
        fields = ('phone_number',)


class MessageForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)


class EmailForm(forms.Form):
    subject = forms.CharField(widget=forms.Textarea)
    text = forms.CharField(widget=forms.Textarea)    
