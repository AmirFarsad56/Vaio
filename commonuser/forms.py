from django import forms
from commonuser.models import CommonUserModel


class CommonUserForm(forms.ModelForm):

    class Meta:
        model = CommonUserModel
        fields = ('first_name','last_name','phone_number','picture')

