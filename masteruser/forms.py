from django import forms
from masteruser.models import MasterUserModel


class MasterUserForm(forms.ModelForm):

    class Meta:
        model = MasterUserModel
        fields = ('phone_number',)
