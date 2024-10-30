from django import forms

from smartphones.models import Smartphone

class SmartphoneForm(forms.ModelForm):
    class Meta:
        model = Smartphone
        fields = ['name_smartphone','marca','ram','storage','Screen_size']
