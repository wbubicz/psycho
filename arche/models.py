# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

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
	odpowiedzi = models.ForeignKey('Odpowiedzi')
	pytanie = models.ForeignKey('Pytanie')
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
	odpowiedzi = models.ForeignKey('Odpowiedzi')
	data = models.DateTimeField(blank=True, null=True)


class Odpowiedzi(models.Model):
	user = models.ForeignKey('auth.User')
	quiz = models.ForeignKey('Quiz')