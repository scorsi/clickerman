from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ValidationError

from .models import *


class LoginForm(AuthenticationForm):
	username = forms.CharField(label="Username", max_length=30,
		widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'Addresse email ou Username'}))
	password = forms.CharField(label="Password", max_length=30,
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'placeholder': 'Mot de passe'}))
	def clean_username(self):
		username = self.data['username']
		if '@' in username:
			try:
				username = User.objects.get(email=username).username
			except ObjectDoesNotExist:
				raise ValidationError(
					self.error_messages['invalid_login'],
					code='invalid_login',
					params={'username':self.username_field.verbose_name},
				)
		return username
