from django import forms
from commonuser.models import CommonUserModel


class CommonUserForm(forms.ModelForm):

    class Meta:
        model = CommonUserModel
        fields = ('phone_number','picture')


class MessageForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)


class EmailForm(forms.Form):
    subject = forms.CharField(widget=forms.Textarea)
    text = forms.CharField(widget=forms.Textarea)


class CommonUserUpdateForm(forms.ModelForm):
    class Meta():
        model = CommonUserModel
        fields = ('phone_number','picture')
