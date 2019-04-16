from django import forms
from commonuser.models import CommonUserModel


class CommonUserForm(forms.ModelForm):

    class Meta:
        model = CommonUserModel
        fields = ('phone_number','picture')
