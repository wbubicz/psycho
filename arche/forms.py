from django import forms
from django.db import models
from django.contrib.auth.models import User

from arche.models import UsernameEmail, ZmianaHasla


class FormularzUser(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password']


class FormularzZapomnialemHasla(forms.ModelForm):
	class Meta:
		model = UsernameEmail
		fields = ['username', 'email']


class FormularzZmianaHasla(forms.ModelForm):
	nowe_haslo1 = forms.CharField(widget=forms.PasswordInput)
	nowe_haslo2 = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = ZmianaHasla
		fields = ['token', 'nowe_haslo1', 'nowe_haslo2']
		widgets = {'password': forms.PasswordInput(),}