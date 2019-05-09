from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserModel


class UserForm(UserCreationForm):
    '''form for creating a user'''

    terms = forms.BooleanField(
    error_messages={'required': 'You must accept terms and conditions'},
    )

    class Meta(UserCreationForm):
        model = UserModel
        fields = ('username','email','first_name',
                  'last_name','password1','password2')


class TypesForm(forms.Form):
    commonusers = forms.BooleanField(required=False)
    masterusers = forms.BooleanField(required=False)
    sportclubs = forms.BooleanField(required=False)


class MessageForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)


class EmailForm(forms.Form):
    subject = forms.CharField(widget=forms.Textarea)
    text = forms.CharField(widget=forms.Textarea)
