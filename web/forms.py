from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ValidationError, ModelForm

from .models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Addresse email ou Nom d\'utilisateur", max_length=30, required=True,
                               widget=forms.EmailInput(attrs={'class': 'login_input', 'name': 'username',
                                                              'placeholder': 'Addresse email ou Nom d\'utilisateur'}))
    password = forms.CharField(label="Mot de passe", max_length=30, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'login_input', 'name': 'password',
                                                                 'placeholder': 'Mot de passe'}))

    def clean_username(self):
        username = self.data['username']
        if '@' in username:
            try:
                username = User.objects.get(email=username).username
            except ObjectDoesNotExist:
                raise ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
        return username


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input_underline', 'name': 'username'}),
            'email': forms.EmailInput(attrs={'class': 'input_underline', 'name': 'email'}),
            'password': forms.PasswordInput(attrs={'class': 'login_input', 'name': 'password'})
        }
