from django.forms import fields
from .models import Don, Besoin
from django import forms
from django.forms.fields import ChoiceField

class DonForm(forms.ModelForm):
    class Meta:
        model = Don
        fields = [
            'type','montant','detail',
        ]

class BesoinForm(forms.ModelForm):
    class Meta:
        model = Besoin
        fields = [
            'type','titre','resume','description',
        ]