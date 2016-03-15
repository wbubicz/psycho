from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

from arche.models import UsernameEmail, ZmianaHasla, ChceZmianyHasla


class FormularzUser(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password']
#
# 	def clean_username(self):
# 		username = self.cleaned_data['username']
# 		if User.objects.filter(username=username).exists():
# 			raise ValidationError('User registered already.')
# 		return username


class FormularzZapomnialemHasla(forms.ModelForm):
	class Meta:
		model = UsernameEmail
		fields = ['username', 'email']


class FormularzZmianaHasla(forms.ModelForm):
	# nowe_haslo1 = forms.CharField(widget=forms.PasswordInput)
	# nowe_haslo2 = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = ZmianaHasla
		fields = ['username', 'token', 'password']
		# widgets = {'password': forms.PasswordInput(),}

class FormularzChceZmianyHasla(forms.ModelForm):
	class Meta:
		model = ChceZmianyHasla
		fields = ['password']
		# widgets = {'password': forms.PasswordInput(),}