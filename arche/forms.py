from django import forms
from django.db import models
from django.contrib.auth.models import User


class FormularzUser(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password']