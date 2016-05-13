from stale import *

def zlicz_python(wyniki, id11, id12, id20, id21, id65, wypis_python, data_quizu):
	for i in range(1, len(nazwy)):
		wypis_python[data_quizu][nazwy[i]] = False

	if wyniki['ICD10_g1'].count(1) >= MIN_GRUPA_1_DEPRESJA_ICD10:
		if wyniki['ICD10_g2'].count(1) >= MIN_GRUPA_2_DEPRESJA_ICD10:
					wypis_python[data_quizu][nazwy[1]] = True
	if wyniki['DSM5_g3'].count(1) >= MIN_GRUPA_3_DEPRESJA_DSM5:
		if id11.odpowiedz == 1 or id12.odpowiedz == 1:
			if id20.odpowiedz == 1 and id21.odpowiedz == 0:
					wypis_python[data_quizu][nazwy[2]] = True
	if wyniki['ICD10_g4'].count(1) >= MIN_GRUPA_4_ANANKASTYCZNE_ICD10:
					wypis_python[data_quizu][nazwy[3]] = True
	if wyniki['DSM5_g5'].count(1) >= MIN_GRUPA_5_ANANKASTYCZNE_DSMIV:
					wypis_python[data_quizu][nazwy[4]] = True
	if wyniki['ICD10_g6'].count(1) >= MIN_GRUPA_6_PARANOICZNA_ICD10:
					wypis_python[data_quizu][nazwy[5]] = True
	if wyniki['DSM5_g7'].count(1) >= MIN_GRUPA_7_PARANOICZNA_DSMIV:
					wypis_python[data_quizu][nazwy[6]] = True
	if wyniki['ICD10_g8'].count(1) >= MIN_GRUPA_8_UNIKOWE_ICD10:
					wypis_python[data_quizu][nazwy[7]] = True
	if wyniki['DSM5_g9'].count(1) >= MIN_GRUPA_9_UNIKOWE_DSMIV:
					wypis_python[data_quizu][nazwy[8]] = True
	if wyniki['ICD10_g11'].count(1) >= MIN_GRUPA_11_ZLU_ICD10:
		if wyniki['ICD10_g12'].count(1) >= MIN_GRUPA_12_ZLU_ICD10:
			if id65.odpowiedz == 1:
					wypis_python[data_quizu][nazwy[9]] = True

	return wypis_python