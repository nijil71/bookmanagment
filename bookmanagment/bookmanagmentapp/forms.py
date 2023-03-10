from django import forms
from .models import *
from django.contrib.auth.models import User


class regform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']

class logform(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

class bookform(forms.ModelForm):
    class Meta:
        model = book
        fields = ['bookname','author','pdf','image','date']
