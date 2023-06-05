from django import forms


class ApplicationDetailForm(forms.Form):
    application_id = forms.IntegerField(label="Application id")