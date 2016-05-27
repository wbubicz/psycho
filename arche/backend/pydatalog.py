import os, sys, inspect
from stale import *
from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, NazwaGrupy, odpowiedz_datalog, choroba_datalog, liczba_odp_tak')

import ast
dane_wejsciowe = sys.argv[1]
wyniki_datalog = ast.literal_eval(dane_wejsciowe)

for grupa in nazwy_grup:
	for i in range(len(wyniki_datalog[grupa])):
		odpowiedz_datalog[grupa,i] = wyniki_datalog[grupa][i]
os.system("touch /home/wbubicz/fefwfef.ss")

# Regula zliczajaca ilosc jedynek w liscie
(liczba_odp_tak[NazwaGrupy]==len_(Y)) <= (odpowiedz_datalog[NazwaGrupy,Y]==1)

wypis_datalog = {}
liczba_wpisow = len(nazwy) - 1 # minus 1 bo w choroba_datalog liczenie jest od 0, a w nazwach od 1
for i in range(liczba_wpisow):
	wypis_datalog[nazwy[i + 1]] = False

for i in range(liczba_wpisow):
	if ((choroba_datalog[nazwy[i+1]]==X).data):
		if (choroba_datalog[nazwy[i+1]]==X).data[0][0]==True:
			wypis_datalog[nazwy[i + 1]] = True

obecny_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0])) + SLASH

wsad = "{'Depresja (DSM-5)': 7, 'Paranoidalne zaburzenie osobowosci (DSM-IV)': True, 'Anankastyczne zaburzenie osobowosci (DSM-IV)': True, 'Paranoidalne zaburzenie osobowosci (ICD-10)': True, 'Histrioniczne zaburzenie osobowosci (DSM-IV)': True, 'Unikowe zaburzenie osobowosci (ICD-10)': True, 'Unikowe zaburzenie osobowosci (DSM-IV)': True, 'Zespol leku uogolnionego (ICD-10)': True, 'Zespol leku uogolnionego (DSM-5)': False, 'Histrioniczne zaburzenie osobowosci (ICD-10)': True, 'Anankastyczne zaburzenie osobowosci (ICD-10)': True, 'Depresja (ICD-10)': True, 'Zaburzenie obsesyjno-kompulsyjne (ICD-10)': True}"
cmd = 'echo "'
cmd = cmd + wsad
cmd = cmd + '" > '
cmd = cmd + "/home/wbubicz/arche/backend/output.txt"
os.system(cmd)

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