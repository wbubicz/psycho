from stale import *

def zlicz_python(wyniki, wypis_python, data_quizu):
	for i in range(1, len(nazwy)):
		wypis_python[data_quizu][nazwy[i]] = False

	if wyniki['ICD10_g1'].count(1) >= MIN_GRUPA_1_DEPRESJA_ICD10:
		if wyniki['ICD10_g2'].count(1) >= MIN_GRUPA_2_DEPRESJA_ICD10:
					wypis_python[data_quizu][nazwy[1]] = True
	if wyniki['DSM5_g3'].count(1) >= MIN_GRUPA_3_DEPRESJA_DSM5:
		if wyniki['DSM5_11'][0] == 1 or wyniki['DSM5_12'][0] == 1:
			if wyniki['DSM5_20'][0] == 1 and wyniki['DSM5_21'][0] == 0:

					wypis_python[data_quizu][nazwy[2]] = True
	if wyniki['ICD10_g4'].count(1) >= MIN_GRUPA_4_ANANKASTYCZNE_ICD10:
					wypis_python[data_quizu][nazwy[3]] = True
	if wyniki['DSMIV_g5'].count(1) >= MIN_GRUPA_5_ANANKASTYCZNE_DSMIV:
					wypis_python[data_quizu][nazwy[4]] = True

	if wyniki['ICD10_g6'].count(1) >= MIN_GRUPA_6_PARANOICZNA_ICD10:
					wypis_python[data_quizu][nazwy[5]] = True
	if wyniki['DSMIV_g7'].count(1) >= MIN_GRUPA_7_PARANOICZNA_DSMIV:
					wypis_python[data_quizu][nazwy[6]] = True

	if wyniki['ICD10_g8'].count(1) >= MIN_GRUPA_8_UNIKOWE_ICD10:
					wypis_python[data_quizu][nazwy[7]] = True
	if wyniki['DSMIV_g9'].count(1) >= MIN_GRUPA_9_UNIKOWE_DSMIV:
					wypis_python[data_quizu][nazwy[8]] = True

	if wyniki['ICD10_g11'].count(1) >= MIN_GRUPA_11_ZLU_ICD10:
		if wyniki['ICD10_g12'].count(1) >= MIN_GRUPA_12_ZLU_ICD10:
			if wyniki['ICD10_65'][0] == 1:
					wypis_python[data_quizu][nazwy[9]] = True
				# trzeba dodac tu i w datalogu ze nie ma ZOK i panicznego
	if wyniki['DSM5_g14'].count(1) >= MIN_GRUPA_14_ZLU_DSM5:
		if wyniki['DSM5_88'][0] == 1 and wyniki['DSM5_96'][0] == 1 and wyniki['DSM5_97'][0] == 0:
					wypis_python[data_quizu][nazwy[10]] = True

	if wyniki['ICD10_g18'].count(1) >= MIN_GRUPA_18_ZOK_ICD10:
		if wyniki['ICD10_98'][0] == 1 and wyniki['ICD10_103'][0] == 1:
					wypis_python[data_quizu][nazwy[11]] = True

	if wyniki['ICD10_g20'].count(1) >= MIN_GRUPA_20_HZO_ICD10:
					wypis_python[data_quizu][nazwy[12]] = True
	if wyniki['DSMIV_g21'].count(1) >= MIN_GRUPA_21_HZO_DSMIV:
					wypis_python[data_quizu][nazwy[13]] = True

	return wypis_python