from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.core.exceptions import ObjectDoesNotExist

from .models import *


class LoginForm(AuthenticationForm):
    def clean_username(self):
        username = self.data['username']
        if '@' in username:
            try:
                user = User.objects.get(email=username)
                username = user.username
            except ObjectDoesNotExist:
                return username
        return username


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email',)
        field_classes = {'username': UsernameField}
        """
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input_underline', 'name': 'username'}),
            'email': forms.EmailInput(attrs={'class': 'input_underline', 'name': 'email'}),
            'password': forms.PasswordInput(attrs={'class': 'login_input', 'name': 'password'})
        }
        """


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('gender', 'medias', 'social_networks', 'bio', 'date_birthday')