from stale import *
from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, NazwaGrupy, odpowiedz_datalog, choroba_datalog, liczba_odp_tak')

def kalkuluj_datalog(wyniki_quizu):
	import globals

	for grupa in nazwy_grup:
		for i in range(len(wyniki_quizu[grupa])):
			odpowiedz_datalog[grupa,i] = wyniki_quizu[grupa][i]

	# Regula zliczajaca ilosc jedynek w liscie
	(liczba_odp_tak[NazwaGrupy]==len_(Y)) <= (odpowiedz_datalog[NazwaGrupy,Y]==1)

	# Depresja (ICD-10) 1
	(choroba_datalog[nazwy[1]]==True) <= (liczba_odp_tak['ICD10_g1']>=MIN_GRUPA_1_DEPRESJA_ICD10)\
												& (liczba_odp_tak['ICD10_g2']>=MIN_GRUPA_2_DEPRESJA_ICD10)
	# Depresja (DSM-IV) 2
	(choroba_datalog[nazwy[2]]==True) <= (liczba_odp_tak['DSMIV_g3']>=MIN_GRUPA_3_DEPRESJA_DSMIV)\
												& ((odpowiedz_datalog['DSMIV_11',0]==1) or (odpowiedz_datalog['DSMIV_12',0]==1))\
												& (odpowiedz_datalog['DSMIV_20',0]==1)\
												& (odpowiedz_datalog['DSMIV_21',0]==0)
	# Anankastyczne zaburzenie osobowosci (ICD-10) 3
	(choroba_datalog[nazwy[3]]==True) <= (liczba_odp_tak['ICD10_g4']>=MIN_GRUPA_4_ANANKASTYCZNE_ICD10)
	# Anankastyczne zaburzenie osobowosci (DSM-IV) 4
	(choroba_datalog[nazwy[4]]==True) <= (liczba_odp_tak['DSMIV_g5']>=MIN_GRUPA_5_ANANKASTYCZNE_DSMIV)
	# Paranoidalne zaburzenie osobowosci (ICD-10) 5
	(choroba_datalog[nazwy[5]]==True) <= (liczba_odp_tak['ICD10_g6']>=MIN_GRUPA_6_PARANOICZNA_ICD10)
	# Paranoidalne zaburzenie osobowosci (DSM-IV) 6
	(choroba_datalog[nazwy[6]]==True) <= (liczba_odp_tak['DSMIV_g7']>=MIN_GRUPA_7_PARANOICZNA_DSMIV)
	# Unikowe zaburzenie osobowosci (ICD-10) 7
	(choroba_datalog[nazwy[7]]==True) <= (liczba_odp_tak['ICD10_g8']>=MIN_GRUPA_8_UNIKOWE_ICD10)
	# Unikowe zaburzenie osobowosci (DSM-IV) 8
	(choroba_datalog[nazwy[8]]==True) <= (liczba_odp_tak['DSMIV_g9']>=MIN_GRUPA_9_UNIKOWE_DSMIV)
	# Zespol leku uogolnionego (ICD-10) 9
	(choroba_datalog[nazwy[9]]==True) <= (liczba_odp_tak['ICD10_g11']>=MIN_GRUPA_11_ZLU_ICD10)\
												& (liczba_odp_tak['ICD10_g12']>=MIN_GRUPA_12_ZLU_ICD10)\
												& (odpowiedz_datalog['ICD10_65',0]==1)
	# Zespol leku uogolnionego (DSM-IV) 10
	(choroba_datalog[nazwy[10]]==True) <= (liczba_odp_tak['DSMIV_g14']>=MIN_GRUPA_14_ZLU_DSMIV)\
												& (odpowiedz_datalog['DSMIV_88',0]==1)\
												& (odpowiedz_datalog['DSMIV_96',0]==1)\
												& (odpowiedz_datalog['DSMIV_97',0]==1)
	# Zaburzenie obsesyjno-kompulsyjne (ICD-10) 11
	(choroba_datalog[nazwy[11]]==True) <= (liczba_odp_tak['ICD10_g18']>=MIN_GRUPA_18_ZOK_ICD10)\
												& (odpowiedz_datalog['ICD10_98',0]==1)\
												& (odpowiedz_datalog['ICD10_103',0]==1)
	# Histrioniczne zaburzenie osobowosci (ICD-10) 12
	(choroba_datalog[nazwy[12]]==True) <= (liczba_odp_tak['ICD10_g20']>=MIN_GRUPA_20_HZO_ICD10)
	# Histrioniczne zaburzenie osobowosci (DSM-IV) 13
	(choroba_datalog[nazwy[13]]==True) <= (liczba_odp_tak['DSMIV_g21']>=MIN_GRUPA_21_HZO_DSMIV)
	# Osobowosc zalezna (ICD-10) 14
	(choroba_datalog[nazwy[14]]==True) <= (liczba_odp_tak['ICD10_g22']>=MIN_GRUPA_22_OZ_ICD10)
	# Osobowosc zalezna (DSM-IV) 15
	(choroba_datalog[nazwy[15]]==True) <= (liczba_odp_tak['DSMIV_g23']>=MIN_GRUPA_23_OZ_DSMIV)
	# Osobowosc schizoidalna (ICD-10) 16
	(choroba_datalog[nazwy[16]]==True) <= (liczba_odp_tak['ICD10_g24']>=MIN_GRUPA_24_OS_ICD10)
	# Osobowosc schizoidalna (DSM-IV) 17
	(choroba_datalog[nazwy[17]]==True) <= (liczba_odp_tak['DSMIV_g25']>=MIN_GRUPA_25_OS_DSMIV)
	# Psychopatia (ICD-10) 18
	(choroba_datalog[nazwy[18]]==True) <= (liczba_odp_tak['ICD10_g28']>=MIN_GRUPA_28_PSYCHOPATIA_ICD10)\
												& (odpowiedz_datalog['ICD10_148',0]==1)\
												& (odpowiedz_datalog['ICD10_149',0]==1)

	wypis_datalog_dla_quizu = {}
	liczba_wpisow = len(nazwy) - 1 # minus 1 bo w choroba_datalog liczenie jest od 0, a w nazwach od 1
	for i in range(liczba_wpisow):
		wypis_datalog_dla_quizu[nazwy[i + 1]] = False

	for i in range(liczba_wpisow):
		if ((choroba_datalog[nazwy[i+1]]==X).data):
			if (choroba_datalog[nazwy[i+1]]==X).data[0][0]==True:
				wypis_datalog_dla_quizu[nazwy[i + 1]] = True

	globals.glob_dict = wypis_datalog_dla_quizu

# from stale import *
# from pyDatalog import pyDatalog
#
# def kalkuluj_datalog(wyniki_quizu):
# 	import globals
#
# 	wypis_datalog_dla_quizu = {}
# 	liczba_wpisow = len(nazwy) - 1 # minus 1 bo w choroba_datalog liczenie jest od 0, a w nazwach od 1
# 	for i in range(liczba_wpisow):
# 		wypis_datalog_dla_quizu[nazwy[i + 1]] = False
#
# 	for i in range(liczba_wpisow):
# 				wypis_datalog_dla_quizu[nazwy[i + 1]] = True
#
# 	globals.glob_dict = wypis_datalog_dla_quizu