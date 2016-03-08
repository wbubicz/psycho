# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django import forms

RODZAJE_ODPOWIEDZI = (
	('TF', 'Prawda albo fałsz'),
	('5S', '5-stopniowa'),
)

KLASYFIKACJE = (
	('ICD-10', 'ICD-10'),
	('DSM-IV', 'DSM-IV'),
)


class Pytanie(models.Model):
	zestaw = models.ForeignKey('Zestaw')
	rodzajOdpowiedzi = models.CharField(max_length=2, choices=RODZAJE_ODPOWIEDZI)
	tresc = models.TextField()
	numer = models.IntegerField()


class Odp(models.Model):
	pytanie = models.ForeignKey('Pytanie')
	quiz = models.ForeignKey('Quiz')
	odpowiedz = models.IntegerField()  # 0-1 dla TF, 1-5 dla 5S itd.


class Zestaw(models.Model):
	choroba = models.ForeignKey('Choroba')
	klasyfikacja = models.CharField(max_length=6, choices=KLASYFIKACJE)


class Choroba(models.Model):
	nazwa = models.TextField()


class Diagnoza(models.Model):
	choroba = models.ForeignKey('Choroba')
	user = models.ForeignKey('auth.User')


class Quiz(models.Model):
	user = models.ForeignKey('auth.User')
	data = models.DateTimeField(blank=True, null=True)


	# class UniqueUserEmailField(forms.EmailField):
	# 	def validate(self, value):
	# 		super(forms.EmailField, self).validate(value)
	# 		try:
	# 			User.objects.get(email=value)
	# 			raise forms.ValidationError("Podany adres e-mail już istnieje.")
	# 		except User.MultipleObjectsReturned:
	# 			raise forms.ValidationError("Podany adres e-mail już istnieje.")
	# 		except User.DoesNotExist:
	# 			pass


	# class MojUserCreationForm(UserCreationForm):
	# 	email = forms.EmailField(required=True)
	#
	# 	username = forms.CharField(required=False, max_length=30)
	# 	email = UniqueUserEmailField(required=True, label='Adres e-mail')
	#
	# 	def __init__(self, *args, **kwargs):
	# 		super(MojUserCreationForm, self).__init__(*args, **kwargs)
	# 		for fieldname in ['username']:
	# 			self.fields[fieldname].help_text = "Bla bla"
	# 			self.fields[fieldname].label = "dsu[a"
	#
	# 	def save(self, commit=True):
	# 		user = super(MojUserCreationForm, self).save(commit=False)
	# 		user.email = self.cleaned_data['email']
	# 		if commit:
	# 			user.save()
	# 		return user
	#
	# 	class Meta:
	# 		model = User
	# 		fields = ("email", "password1", "password2")