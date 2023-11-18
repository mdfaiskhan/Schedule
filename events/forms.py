from dataclasses import fields
from django import forms

from .models import Events
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email']
        
class Event(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('title','date','time','venue','description','email','image','id')

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)