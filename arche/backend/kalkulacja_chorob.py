# -*- coding: utf-8 -*-

# encoding=utf8
import inspect
import os
import sys
import time
from zliczanie_python import zlicz_python

from arche.backend.stale import *
from arche.models import Odp
obecny_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
obecny_folder = obecny_folder[:-8]
if obecny_folder not in sys.path:
	sys.path.insert(0, obecny_folder)

# from arche.datalog.reguly import *

reload(sys)
sys.setdefaultencoding('utf8')

wyniki = {}

def kalkuluj_choroby(quizy):
	choroby_uogolnione_python = []
	choroby_uogolnione_datalog = []
	wypis_python = {}
	wypis_datalog = {}
	czas_python = 0
	czas_datalog = 0
	odp = Odp()
	id11, id12, id20, id21, id65 = odp, odp, odp, odp, odp
	for quiz in quizy:
		wyniki_quizu = {}
		data_quizu = str(quiz.data)
		wypis_python[data_quizu] = {}
		wypis_datalog[data_quizu] = {}

		# DEPRESJA: ICD10: 2 z grupy pierwszej oraz 2 z grupy 2, DSMIV: 5 z grupy 3, id11 lub id12, 20, ~21

		icd10g1 = Odp.objects.filter(quiz=quiz, klasyfikacja='ICD-10', grupa=1)
		numer_nazwy_grupy = 0
		odpowiedzi_do_przepisania = []
		for odpowiedz in icd10g1:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki_quizu[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		icd10g2 = Odp.objects.filter(quiz=quiz, klasyfikacja='ICD-10', grupa=2)
		numer_nazwy_grupy = 1
		odpowiedzi_do_przepisania = []
		for odpowiedz in icd10g2:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki_quizu[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		dsm4g3 = Odp.objects.filter(quiz=quiz, klasyfikacja='DSM-IV', grupa=3)
		numer_nazwy_grupy = 2
		odpowiedzi_do_przepisania = []
		for odpowiedz in dsm4g3:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki_quizu[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		try:
			id11 = Odp.objects.get(quiz=quiz, id_pytania=11)
			temp = []
			temp.append(id11.odpowiedz)
			wyniki_quizu[nazwy_grup[3]] = temp
			id12 = Odp.objects.get(quiz=quiz, id_pytania=12)
			temp = []
			temp.append(id12.odpowiedz)
			wyniki_quizu[nazwy_grup[4]] = temp
			id20 = Odp.objects.get(quiz=quiz, id_pytania=20)
			temp = []
			temp.append(id20.odpowiedz)
			wyniki_quizu[nazwy_grup[5]] = temp
			id21 = Odp.objects.get(quiz=quiz, id_pytania=21)
			temp = []
			temp.append(id21.odpowiedz)
			wyniki_quizu[nazwy_grup[6]] = temp

		except:
			pass

		# ANANKASTYCZNE ZABURZENIE: ICD10: min 4, DSM4: min 4, grupy: 4, 5

		icd10g4 = Odp.objects.filter(quiz=quiz, klasyfikacja='ICD-10', grupa=4)
		numer_nazwy_grupy = 7
		odpowiedzi_do_przepisania = []
		for odpowiedz in icd10g4:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki_quizu[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		dsm4g5 = Odp.objects.filter(quiz=quiz, klasyfikacja='DSM-IV', grupa=5)
		numer_nazwy_grupy = 8
		odpowiedzi_do_przepisania = []
		for odpowiedz in dsm4g5:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki_quizu[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		# OSOBOWOSC PARANOICZNA, powiedzmy po 4 z 7 kazdego testu, grupy: 6, 7

		icd10g6 = Odp.objects.filter(quiz=quiz, klasyfikacja='ICD-10', grupa=6)
		numer_nazwy_grupy = 9
		odpowiedzi_do_przepisania = []
		for odpowiedz in icd10g6:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki_quizu[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		dsm4g7 = Odp.objects.filter(quiz=quiz, klasyfikacja='DSM-IV', grupa=7)
		numer_nazwy_grupy = 10
		odpowiedzi_do_przepisania = []
		for odpowiedz in dsm4g7:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki_quizu[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		# UNIKOWE ZABURZENIE OSOBOWOSCI: ICD10: min 4, DSM4: min 4, grupy: 8, 9

		icd10g8 = Odp.objects.filter(quiz=quiz, klasyfikacja='ICD-10', grupa=8)
		numer_nazwy_grupy = 11
		odpowiedzi_do_przepisania = []
		for odpowiedz in icd10g8:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki_quizu[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		dsm4g9 = Odp.objects.filter(quiz=quiz, klasyfikacja='DSM-IV', grupa=9)
		numer_nazwy_grupy = 12
		odpowiedzi_do_przepisania = []
		for odpowiedz in dsm4g9:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki_quizu[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		# ZESPOL LEKU UOGOLNIONEGO: ICD10: 65, 1 z g11, 3 z g12, nie lek paniczny i nie ZOK, DSMIV:

		try:
			id65 = Odp.objects.get(quiz=quiz, id_pytania=65)
			temp = []
			temp.append(id65.odpowiedz)
			wyniki_quizu[nazwy_grup[13]] = temp
		except:
			pass
		icd10g11 = Odp.objects.filter(quiz=quiz, klasyfikacja='ICD-10', grupa=11)
		numer_nazwy_grupy = 14
		odpowiedzi_do_przepisania = []
		for odpowiedz in icd10g11:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki_quizu[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		icd10g12 = Odp.objects.filter(quiz=quiz, klasyfikacja='ICD-10', grupa=12)
		numer_nazwy_grupy = 15
		odpowiedzi_do_przepisania = []
		for odpowiedz in icd10g12:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki_quizu[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		try:
			id88 = Odp.objects.get(quiz=quiz, id_pytania=88)
			temp = []
			temp.append(id88.odpowiedz)
			wyniki_quizu[nazwy_grup[16]] = temp
			id96 = Odp.objects.get(quiz=quiz, id_pytania=96)
			temp = []
			temp.append(id96.odpowiedz)
			wyniki_quizu[nazwy_grup[18]] = temp
			id97 = Odp.objects.get(quiz=quiz, id_pytania=97)
			temp = []
			temp.append(id97.odpowiedz)
			wyniki_quizu[nazwy_grup[19]] = temp
		except:
			pass
		dsm4g14 = Odp.objects.filter(quiz=quiz, klasyfikacja='DSM-IV', grupa=14)
		numer_nazwy_grupy = 17
		odpowiedzi_do_przepisania = []
		for odpowiedz in dsm4g14:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki_quizu[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		# ZABURZENIE OBSESYJNO-KOMPULSYJNE: ICD10: 98, 4 z g18, 103

		try:
			id98 = Odp.objects.get(quiz=quiz, id_pytania=98)
			id103 = Odp.objects.get(quiz=quiz, id_pytania=103)
			temp = []
			temp.append(id98.odpowiedz)
			wyniki_quizu[nazwy_grup[20]] = temp
			temp = []
			temp.append(id103.odpowiedz)
			wyniki_quizu[nazwy_grup[22]] = temp
		except:
			pass
		icd10g18 = Odp.objects.filter(quiz=quiz, klasyfikacja='ICD-10', grupa=18)
		numer_nazwy_grupy = 21
		odpowiedzi_do_przepisania = []
		for odpowiedz in icd10g18:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki_quizu[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		# HISTRIONICZNE ZABURZENIE OSOBOWOSCI: ICD 3 z g20, DSM-IV: 5 z g21

		icd10g20 = Odp.objects.filter(quiz=quiz, klasyfikacja='ICD-10', grupa=20)
		numer_nazwy_grupy = 23
		odpowiedzi_do_przepisania = []
		for odpowiedz in icd10g20:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki_quizu[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		dsm4g21 = Odp.objects.filter(quiz=quiz, klasyfikacja='DSM-IV', grupa=21)
		numer_nazwy_grupy = 24
		odpowiedzi_do_przepisania = []
		for odpowiedz in dsm4g21:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki_quizu[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		# OSOBOWOSC ZALEZNA

		icd10g22 = Odp.objects.filter(quiz=quiz, klasyfikacja='ICD-10', grupa=22)
		numer_nazwy_grupy = 25
		odpowiedzi_do_przepisania = []
		for odpowiedz in icd10g22:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki_quizu[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		dsm4g23 = Odp.objects.filter(quiz=quiz, klasyfikacja='DSM-IV', grupa=23)
		numer_nazwy_grupy = 26
		odpowiedzi_do_przepisania = []
		for odpowiedz in dsm4g23:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki_quizu[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		# OSOBOWOSC SCHIZOIDALNA

		icd10g24 = Odp.objects.filter(quiz=quiz, klasyfikacja='ICD-10', grupa=24)
		numer_nazwy_grupy = 27
		odpowiedzi_do_przepisania = []
		for odpowiedz in icd10g24:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki_quizu[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		dsm4g25 = Odp.objects.filter(quiz=quiz, klasyfikacja='DSM-IV', grupa=25)
		numer_nazwy_grupy = 28
		odpowiedzi_do_przepisania = []
		for odpowiedz in dsm4g25:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki_quizu[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		# PSYCHOPATIA

		try:
			id148 = Odp.objects.get(quiz=quiz, id_pytania=148)
			id149 = Odp.objects.get(quiz=quiz, id_pytania=149)
			temp = []
			temp.append(id148.odpowiedz)
			wyniki_quizu[nazwy_grup[29]] = temp
			temp = []
			temp.append(id149.odpowiedz)
			wyniki_quizu[nazwy_grup[30]] = temp
		except:
			pass
		icd10g28 = Odp.objects.filter(quiz=quiz, klasyfikacja='ICD-10', grupa=28)
		numer_nazwy_grupy = 31
		odpowiedzi_do_przepisania = []
		for odpowiedz in icd10g28:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki_quizu[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania


		# KALKULACJA PYTHON

		czas_start = time.time()
		wypis_python = zlicz_python(wyniki_quizu, wypis_python, data_quizu)
		czas_koniec = time.time()
		czas_python = czas_koniec - czas_start
		czas_python = "{:.12f}".format(czas_python)



		# KALKULACJA DATALOG

		czas_start = time.time()
		import globals
		import pydatalog
		globals.init()
		pydatalog.kalkuluj_datalog(wyniki_quizu)
		wypis_datalog_dla_quizu = globals.glob_dict

		wypis_datalog[data_quizu] = wypis_datalog_dla_quizu
		czas_koniec = time.time()
		czas_datalog = czas_koniec - czas_start
		czas_datalog = "{:.12f}".format(czas_datalog)



		temp = {}
		for choroba_uogolniona in nazwy_uogolnione:
			temp[choroba_uogolniona] = False
		# Choroby uogolnione, Python
		if wypis_python[data_quizu][nazwy[1]] or wypis_python[data_quizu][nazwy[2]]:
			temp[nazwy_uogolnione[2]] = True
		if wypis_python[data_quizu][nazwy[3]] or wypis_python[data_quizu][nazwy[4]]:
			temp[nazwy_uogolnione[3]] = True
		if wypis_python[data_quizu][nazwy[5]] or wypis_python[data_quizu][nazwy[6]]:
			temp[nazwy_uogolnione[4]] = True
		if wypis_python[data_quizu][nazwy[7]] or wypis_python[data_quizu][nazwy[8]]:
			temp[nazwy_uogolnione[5]] = True
		if wypis_python[data_quizu][nazwy[9]]:
			temp[nazwy_uogolnione[6]] = True

		if temp.values().count(True) > 1: # wiecej niz jedna choroba
			choroby_uogolnione_python.append(nazwy_uogolnione[1])
		elif not True in temp.values(): # zero chorob
			choroby_uogolnione_python.append(nazwy_uogolnione[0])
		else: # jedna choroba
			for numer in range(1, 5):
				choroba_uogolniona = nazwy_uogolnione[numer]
				if temp[choroba_uogolniona] == True:
					choroby_uogolnione_python.append(choroba_uogolniona)
					break
		# Choroby uogolnione, Datalog
		if wypis_datalog_dla_quizu[nazwy[1]] or wypis_datalog_dla_quizu[nazwy[2]]:
			choroby_uogolnione_datalog.append(nazwy_uogolnione[1])
		if wypis_datalog_dla_quizu[nazwy[3]] or wypis_datalog_dla_quizu[nazwy[4]]:
			choroby_uogolnione_datalog.append(nazwy_uogolnione[2])
		if wypis_datalog_dla_quizu[nazwy[4]] or wypis_datalog_dla_quizu[nazwy[6]]:
			choroby_uogolnione_datalog.append(nazwy_uogolnione[3])
		if wypis_datalog_dla_quizu[nazwy[7]] or wypis_datalog_dla_quizu[nazwy[8]]:
			choroby_uogolnione_datalog.append(nazwy_uogolnione[4])
		if not True in wypis_datalog_dla_quizu:
			choroby_uogolnione_datalog.append(nazwy_uogolnione[0])

	return (wypis_python, choroby_uogolnione_python, wypis_datalog, czas_python, czas_datalog)