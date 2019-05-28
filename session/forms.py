from django import forms


class DaysForm(forms.Form):
    length = forms.IntegerField(required=False)
    saturdays = forms.BooleanField(required = False)
    sundays = forms.BooleanField(required = False)
    mondays = forms.BooleanField(required = False)
    tuesdays = forms.BooleanField(required = False)
    wednesdays = forms.BooleanField(required = False)
    thursdays = forms.BooleanField(required = False)
    fridays = forms.BooleanField(required = False)


class TimesForm(forms.Form):
    start_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    duration = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    stop_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
