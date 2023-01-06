from django import forms
from .models import Regions, Areas


class ContactForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(required=True)


class CreateRegionForm(forms.ModelForm):
    class Meta:
        model = Regions
        fields = "__all__"


class CreateAreasForm(forms.ModelForm):
    class Meta:
        model = Areas
        fields = "__all__"
