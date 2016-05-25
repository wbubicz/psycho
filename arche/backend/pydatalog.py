import os, sys, inspect
obecny_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
obecny_folder = obecny_folder[:-8] # obetnie "\datalog"
if obecny_folder not in sys.path:
	sys.path.insert(0, obecny_folder)

from stale import *
from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, NazwaGrupy, odpowiedz_datalog, choroba_datalog, liczba_odp_tak')

import ast
dane_wejsciowe = sys.argv[1]
wyniki_datalog = ast.literal_eval(dane_wejsciowe)

for grupa in nazwy_grup:
	for i in range(len(wyniki_datalog[grupa])):
		odpowiedz_datalog[grupa,i] = wyniki_datalog[grupa][i]

# Regula zliczajaca ilosc jedynek w liscie
(liczba_odp_tak[NazwaGrupy]==len_(Y)) <= (odpowiedz_datalog[NazwaGrupy,Y]==1)

# Depresja (ICD-10) 1
(choroba_datalog[nazwy[1]]==True) <= (liczba_odp_tak['ICD10_g1']>=MIN_GRUPA_1_DEPRESJA_ICD10)\
											& (liczba_odp_tak['ICD10_g2']>=MIN_GRUPA_2_DEPRESJA_ICD10)
# Depresja (DSM-5) 2
(choroba_datalog[nazwy[2]]==True) <= (liczba_odp_tak['DSM5_g3']>=MIN_GRUPA_3_DEPRESJA_DSM5)\
											& ((odpowiedz_datalog['DSM5_11',0]==1) or (odpowiedz_datalog['DSM5_12',0]==1))\
											& (odpowiedz_datalog['DSM5_20',0]==1)\
											& (odpowiedz_datalog['DSM5_21',0]==0)
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
# Zespol leku uogolnionego (DSM-5) 10
(choroba_datalog[nazwy[10]]==True) <= (liczba_odp_tak['DSM5_g14']>=MIN_GRUPA_14_ZLU_DSM5)\
											& (odpowiedz_datalog['DSM5_88',0]==1)\
											& (odpowiedz_datalog['DSM5_96',0]==1)\
											& (odpowiedz_datalog['DSM5_97',0]==0)
# Zaburzenie obsesyjno-kompulsyjne (ICD-10) 11
(choroba_datalog[nazwy[11]]==True) <= (liczba_odp_tak['ICD10_g18']>=MIN_GRUPA_18_ZOK_ICD10)\
											& (odpowiedz_datalog['ICD10_98',0]==1)\
											& (odpowiedz_datalog['ICD10_103',0]==1)
# Histrioniczne zaburzenie osobowosci (ICD-10) 12
(choroba_datalog[nazwy[12]]==True) <= (liczba_odp_tak['ICD10_g20']>=MIN_GRUPA_20_HZO_ICD10)
# Histrioniczne zaburzenie osobowosci (DSM-IV) 13
(choroba_datalog[nazwy[13]]==True) <= (liczba_odp_tak['DSMIV_g21']>=MIN_GRUPA_21_HZO_DSMIV)

wypis_datalog = {}
liczba_wpisow = len(nazwy) - 1 # minus 1 bo w choroba_datalog liczenie jest od 0, a w nazwach od 1
for i in range(liczba_wpisow):
	wypis_datalog[nazwy[i + 1]] = False

for i in range(liczba_wpisow):
	if ((choroba_datalog[nazwy[i+1]]==X).data):
		if (choroba_datalog[nazwy[i+1]]==X).data[0][0]==True:
			wypis_datalog[nazwy[i + 1]] = True

obecny_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0])) + SLASH

os.system("rm "+obecny_folder+"output.txt")
os.system("touch "+obecny_folder+"output.txt")
os.system("chmod 777 "+obecny_folder+"output.txt")
wsad = "{'Depresja (DSM-5)': 7, 'Paranoidalne zaburzenie osobowosci (DSM-IV)': True, 'Anankastyczne zaburzenie osobowosci (DSM-IV)': True, 'Paranoidalne zaburzenie osobowosci (ICD-10)': True, 'Histrioniczne zaburzenie osobowosci (DSM-IV)': True, 'Unikowe zaburzenie osobowosci (ICD-10)': True, 'Unikowe zaburzenie osobowosci (DSM-IV)': True, 'Zespol leku uogolnionego (ICD-10)': True, 'Zespol leku uogolnionego (DSM-5)': False, 'Histrioniczne zaburzenie osobowosci (ICD-10)': True, 'Anankastyczne zaburzenie osobowosci (ICD-10)': True, 'Depresja (ICD-10)': True, 'Zaburzenie obsesyjno-kompulsyjne (ICD-10)': True}"
gogo = 'echo "'
gogo = gogo + wsad
gogo = gogo + '" > '
gogo = gogo + +obecny_folder
gogo = gogo + "output.txt"
os.system(gogo)

# try:
# 	os.remove(obecny_folder+'output.txt')
# except:
# 	pass
# os.open(obecny_folder+'output.txt', os.O_CREAT)
# do_outputu = str(wypis_datalog)
# plik = os.open(obecny_folder+'output.txt', os.O_RDWR)
# os.write(plik, do_outputu)
# os.fsync(plik)
# os.close(plik)

# pierwotny_stdout = sys.stdout
# obecny_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0])) + SLASH
# sys.stdout = open(obecny_folder+'output.txt', 'w') # Wynik skryptu do output.txt
# print wypis_datalog
# sys.stdout = pierwotny_stdout # restore the previous stdout.