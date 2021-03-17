from django import forms
from .models import Properites
class vechileForm(forms.ModelForm):
    class Meta:
        model=Properites
        fields=['vechile_name','vechile_series','vechile_price','vechile_description','vechile_image']