from django import forms
from django.db import models
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['email', ]