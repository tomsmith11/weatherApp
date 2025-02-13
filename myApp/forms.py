from django import forms
from django.forms import ModelForm, TextInput
from .models import City

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']
        lables = {'name': 'Name'}
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        } 