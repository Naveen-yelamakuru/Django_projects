from django import forms
from . models import poject

class project_form(forms.ModelForm):
    class Meta:
        model=poject
        fields=['project_name','project_price','project_author','project_description']