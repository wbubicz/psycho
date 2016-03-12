# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django import forms

import re

RODZAJE_ODPOWIEDZI = (
	('TF', 'Prawda albo fałsz'),
	('5S', '5-stopniowa'),
)

KLASYFIKACJE = (
	('ICD-10', 'ICD-10'),
	('DSM-IV', 'DSM-IV'),
	('DSM-5', 'DSM-5'),
)


# class Choroba(models.Model):
# 	nazwa = models.TextField()


# class Zestaw(models.Model):
# 	choroba = models.ForeignKey('Choroba')
# 	klasyfikacja = models.CharField(max_length=6, choices=KLASYFIKACJE)


# class Diagnoza(models.Model):
# 	choroba = models.ForeignKey('Choroba')
# 	user = models.ForeignKey('auth.User')


# class Grupa(models.Model):
# 	zestaw = models.ForeignKey('Zestaw')
# 	opis = models.CharField(max_length=200)  # Czy przez co najmniej dwa tygodnie
# 	# występował u Pana/Pani któryś z następujących objawów?
# 	kod = models.CharField(max_length=20)  # EPR1I, EPR2I, ABO1D itp.
# 	minimum = models.IntegerField()

class Opis(models.Model):
	tresc = models.TextField()


# class Pytanie(models.Model):
# 	grupa = models.ForeignKey('Grupa')
# 	rodzajOdpowiedzi = models.CharField(max_length=2, choices=RODZAJE_ODPOWIEDZI)
# 	tresc = models.TextField()
# 	numer = models.IntegerField()

class Pytanie(models.Model):
	numer = models.CharField(max_length=3)
	tresc = models.TextField()
	rodzajOdpowiedzi = models.CharField(max_length=2, choices=RODZAJE_ODPOWIEDZI)
	klasyfikacja = models.CharField(max_length=6, choices=KLASYFIKACJE)
	grupa = models.IntegerField(null=True)
	choroba = models.TextField()
	opis = models.ForeignKey('Opis', null=True)


class Odp(models.Model):
	numer = models.CharField(max_length=3)
	tresc = models.TextField(null=True)
	rodzajOdpowiedzi = models.CharField(max_length=2, choices=RODZAJE_ODPOWIEDZI)
	klasyfikacja = models.CharField(max_length=6, choices=KLASYFIKACJE)
	grupa = models.IntegerField(null=True)
	choroba = models.TextField()
	id_pytania = models.IntegerField(null=True)
	quiz = models.ForeignKey('Quiz')
	odpowiedz = models.IntegerField()  # 0-1 dla TF, 1-5 dla 5S itd.


class Quiz(models.Model):
	user = models.ForeignKey('auth.User')
	data = models.DateTimeField(blank=True, null=True)


# class Odp(models.Model):
# 	pytanie = models.ForeignKey('Pytanie')
# 	quiz = models.ForeignKey('Quiz')
# 	odpowiedz = models.IntegerField()  # 0-1 dla TF, 1-5 dla 5S itd.


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


class UsernameEmail(models.Model):
	username = models.CharField(max_length=30)
	email = models.EmailField()


def validate_password(password):
	if len(password) < 8:
		raise ValidationError("30 characters or fewer. Letters, digits and @/./+/-/_ only.")
	if not re.match(r'[A-Za-z0-9@.+-_]{8,}', password):
		raise ValidationError("30 characters or fewer. Letters, digits and @/./+/-/_ only.")


class ZmianaHasla(models.Model):
	username = models.CharField(max_length=30)
	token = models.CharField(max_length=21)
	password = models.CharField(max_length=30, validators=[validate_password])