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


class BankInfoForm(forms.ModelForm):
    class Meta():
        model = SportClubModel
        fields = ('bankaccount_ownername','bankaccount_accountnumber',
                  'bankaccount_cardnumber','bankaccount_shabanumber',
                  'bankaccount_bankname')


class SportClubUpdateForm(forms.ModelForm):
    class Meta():
        model = SportClubModel
        fields = ('phone_number','address','info','picture',)


class TermsAndConditionsForm(forms.ModelForm):
    class Meta():
        model = SportClubModel
        fields = ('terms_and_conditions',)
