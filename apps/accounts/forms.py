from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.db import transaction
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import EmailValidator

from .models import User


class SignUpForm(UserCreationForm):
  
    class Meta(UserCreationForm):

        model = User
        fields = ['email', 'full_name',]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['full_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

    

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['email', 'full_name',]


class SignInForm(AuthenticationForm):
   
    class Meta:
        model = User
        fields = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

    