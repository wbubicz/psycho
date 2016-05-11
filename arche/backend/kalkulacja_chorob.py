# -*- coding: utf-8 -*-

# encoding=utf8
from arche.stale import *

from arche.models import Pytanie, Odp, Quiz, Opis
import ast
from pyDatalog import pyDatalog

import os, sys, inspect
obecny_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
obecny_folder = obecny_folder[:-8]
if obecny_folder not in sys.path:
	sys.path.insert(0, obecny_folder)

# from arche.datalog.reguly import *

reload(sys)
sys.setdefaultencoding('utf8')



def kalkuluj_choroby(quizy):
	wyniki = {}
	choroby_uogolnione_python = {}
	choroby_uogolnione_datalog = {}
	wypis_python = {}
	wypis_datalog = {}
	for quiz in quizy:
		data_quizu = str(quiz.data)
		wypis_python[data_quizu] = {}
		wypis_datalog[data_quizu] = {}
		choroby_uogolnione_python[data_quizu] = {}
		choroby_uogolnione_datalog[data_quizu] = {}

		# DEPRESJA: ICD10: 2 z grupy pierwszej oraz 2 z grupy 2, DSM5: 5 z grupy 3, id11 lub id12, 20, ~21

		icd10g1 = Odp.objects.filter(quiz=quiz, klasyfikacja='ICD-10', grupa=1)
		numer_nazwy_grupy = 0
		odpowiedzi_do_przepisania = []
		for odpowiedz in icd10g1:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		icd10g2 = Odp.objects.filter(quiz=quiz, klasyfikacja='ICD-10', grupa=2)
		numer_nazwy_grupy = 1
		odpowiedzi_do_przepisania = []
		for odpowiedz in icd10g2:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		dsm5g3 = Odp.objects.filter(quiz=quiz, klasyfikacja='DSM-5', grupa=3)
		numer_nazwy_grupy = 2
		odpowiedzi_do_przepisania = []
		for odpowiedz in dsm5g3:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		if wyniki['ICD10_g1'].count(1) >= MIN_GRUPA_1_DEPRESJA_ICD10 and wyniki['ICD10_g2'].count(1) >= MIN_GRUPA_2_DEPRESJA_ICD10:
			wypis_python[data_quizu][nazwy[1]] = True

		try:
			id11 = Odp.objects.get(quiz=quiz, id_pytania=11)
			temp = []
			temp.append(id11.odpowiedz)
			wyniki[nazwy_grup[3]] = temp
			id12 = Odp.objects.get(quiz=quiz, id_pytania=12)
			temp = []
			temp.append(id12.odpowiedz)
			wyniki[nazwy_grup[4]] = temp
			id20 = Odp.objects.get(quiz=quiz, id_pytania=20)
			temp = []
			temp.append(id20.odpowiedz)
			wyniki[nazwy_grup[5]] = temp
			id21 = Odp.objects.get(quiz=quiz, id_pytania=21)
			temp = []
			temp.append(id21.odpowiedz)
			wyniki[nazwy_grup[6]] = temp
			if wyniki['DSM5_g1'].count(1) >= MIN_GRUPA_3_DEPRESJA_DSM5:
				if id11.odpowiedz == 1 or id12.odpowiedz == 1:
					if id20.odpowiedz == 1 and id21.odpowiedz == 0:
						wypis_python[data_quizu][nazwy[2]] = True
		except:
			pass

		# ANANKASTYCZNE ZABURZENIE: ICD10: min 4, DSM4: min 4, grupy: 4, 5

		icd10g4 = Odp.objects.filter(quiz=quiz, klasyfikacja='ICD-10', grupa=4)
		numer_nazwy_grupy = 7
		odpowiedzi_do_przepisania = []
		for odpowiedz in icd10g4:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		dsm4g5 = Odp.objects.filter(quiz=quiz, klasyfikacja='DSM-IV', grupa=5)
		numer_nazwy_grupy = 8
		odpowiedzi_do_przepisania = []
		for odpowiedz in dsm4g5:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		if wyniki['ICD10_g4'].count(1) >= MIN_GRUPA_4_ANANKASTYCZNE_ICD10:
			wypis_python[data_quizu][nazwy[3]] = True
		if wyniki['DSM5_g5'].count(1) >= MIN_GRUPA_5_ANANKASTYCZNE_DSMIV:
			wypis_python[data_quizu][nazwy[4]] = True

		# OSOBOWOSC PARANOICZNA, powiedzmy po 4 z 7 kazdego testu, grupy: 6, 7

		icd10g6 = Odp.objects.filter(quiz=quiz, klasyfikacja='ICD-10', grupa=6)
		numer_nazwy_grupy = 9
		odpowiedzi_do_przepisania = []
		for odpowiedz in icd10g6:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		dsm4g7 = Odp.objects.filter(quiz=quiz, klasyfikacja='DSM-IV', grupa=7)
		numer_nazwy_grupy = 10
		odpowiedzi_do_przepisania = []
		for odpowiedz in dsm4g7:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		if wyniki['ICD10_g6'].count(1) >= MIN_GRUPA_6_PARANOICZNA_ICD10:
			wypis_python[data_quizu][nazwy[5]] = True
		if wyniki['DSM5_g7'].count(1) >= MIN_GRUPA_7_PARANOICZNA_DSMIV:
			wypis_python[data_quizu][nazwy[6]] = True

		# UNIKOWE ZABURZENIE OSOBOWOSCI: ICD10: min 4, DSM4: min 4, grupy: 8, 9

		icd10g8 = Odp.objects.filter(quiz=quiz, klasyfikacja='ICD-10', grupa=8)
		numer_nazwy_grupy = 11
		odpowiedzi_do_przepisania = []
		for odpowiedz in icd10g8:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		dsm4g9 = Odp.objects.filter(quiz=quiz, klasyfikacja='DSM-IV', grupa=9)
		numer_nazwy_grupy = 12
		odpowiedzi_do_przepisania = []
		for odpowiedz in dsm4g9:
			odpowiedzi_do_przepisania.append(odpowiedz.odpowiedz)
		wyniki[nazwy_grup[numer_nazwy_grupy]] = odpowiedzi_do_przepisania

		if wyniki['ICD10_g8'].count(1) >= MIN_GRUPA_8_UNIKOWE_ICD10:
			wypis_python[data_quizu][nazwy[7]] = True
		if wyniki['DSM5_g9'].count(1) >= MIN_GRUPA_9_UNIKOWE_DSMIV:
			wypis_python[data_quizu][nazwy[8]] = True

		obecny_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0])) + "\\"

		wyniki_as_string = str(wyniki)
		os.system("python "+obecny_folder+"reguly.py " + '"' + wyniki_as_string + '"')

		with open(obecny_folder+'output.txt', 'r') as myfile:
			output = myfile.read().replace('\n', '')

		wypis_datalog_dla_quizu = ast.literal_eval(output)
		wypis_datalog[data_quizu] = wypis_datalog_dla_quizu

		# Choroby uogolnione, Python
		if wypis_python[data_quizu][nazwy[1]] or wypis_python[data_quizu][nazwy[2]]:
			choroby_uogolnione_python[data_quizu][1] = True
		if wypis_python[data_quizu][nazwy[3]] or wypis_python[data_quizu][nazwy[4]]:
			choroby_uogolnione_python[data_quizu][2] = True
		if wypis_python[data_quizu][nazwy[5]] or wypis_python[data_quizu][nazwy[6]]:
			choroby_uogolnione_python[data_quizu][3] = True
		if wypis_python[data_quizu][nazwy[7]] or wypis_python[data_quizu][nazwy[8]]:
			choroby_uogolnione_python[data_quizu][4] = True
		# Choroby uogolnione, Datalog
		if wypis_datalog_dla_quizu[nazwy[1]] or wypis_datalog_dla_quizu[nazwy[2]]:
			choroby_uogolnione_datalog[data_quizu][1] = True
		if wypis_datalog_dla_quizu[nazwy[3]] or wypis_datalog_dla_quizu[nazwy[4]]:
			choroby_uogolnione_datalog[data_quizu][2] = True
		if wypis_datalog_dla_quizu[nazwy[4]] or wypis_datalog_dla_quizu[nazwy[6]]:
			choroby_uogolnione_datalog[data_quizu][3] = True
		if wypis_datalog_dla_quizu[nazwy[7]] or wypis_datalog_dla_quizu[nazwy[8]]:
			choroby_uogolnione_datalog[data_quizu][4] = True

	# DWA SLESZE TRZEBA JAKOS GLOBALNIE DO ZMIENNEJ WSTAWIC BO INACZEJ BEDZIE DLA LINUXA INACZEJ DLA WINSOWSA!!!!!!!

	return (wypis_python, choroby_uogolnione_python, wypis_datalog)

