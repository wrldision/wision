from django.forms import fields
from .models import Partenaire
from django import forms
from django.forms.fields import ChoiceField

class PartenaireForm(forms.ModelForm):
    class Meta:
        model = Partenaire
        fields = [
            'nom_organisation','logo_partenaire','description','email1',
            'email2','tel1','tel2',
        ]
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.fields['presentation'].widget.attrs = {'rows': 11}