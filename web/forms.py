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

class AuthenticationForm(forms.Form):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'class': "login_input"})
    )
    password = forms.CharField(widget=forms.PasswordInput)

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


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form_field', 'name': 'username'}),
            'first_name': forms.TextInput(attrs={'class': 'form_field', 'name': 'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'form_field', 'name': 'last_name'}),
            'email': forms.EmailInput(attrs={'class': 'form_field', 'name': 'email'})
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('gender', 'medias', 'social_networks', 'bio', 'date_birthday')
        widgets = {
            'gender': forms.Select(attrs={'class': 'form_field', 'name': 'gender'})
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
