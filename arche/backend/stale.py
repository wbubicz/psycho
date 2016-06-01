# -*- coding: utf-8 -*-
# encoding=utf8

nazwy_grup = [	# ICD
					# DSM
						# Single
				# DEPRESJA
				'ICD10_g1', # 0					grupa 1
				'ICD10_g2', # 1					grupa 2
					'DSM5_g3', # 2				grupa 3
						'DSM5_11', # 3			grupa 0
						'DSM5_12', # 4				  0
						'DSM5_20', # 5				  0
						'DSM5_21', # 6				  0
				# ANANKASTYCZNE ZABURZENIE
				'ICD10_g4', # 7					grupa 4
					'DSMIV_g5', # 8				grupa 5
				# OSOBOWOSC PARANOICZNA
				'ICD10_g6', # 9					grupa 6
					'DSMIV_g7', # 10			grupa 7
				# UNIKOWE ZABURZENIE OSOBOWOSCI
				'ICD10_g8', # 11				grupa 8
					'DSMIV_g9', # 12			grupa 9
				# ZESPOL LEKU UOGOLNIONEGO
						'ICD10_65', # 13		grupa 10
				'ICD10_g11', # 14				grupa 11
				'ICD10_g12', # 15				grupa 12
						'DSM5_88', # 16			grupa 13
					'DSM5_g14', # 17			grupa 14
						'DSM5_96', # 18			grupa 15
						'DSM5_97', # 19			grupa 16
				# ZABURZENIE OBSESYJNO-KOMPULSYJNE
				'ICD10_98', # 20				grupa 17
				'ICD10_g18', # 21				grupa 18
						'ICD10_103', # 22		grupa 19
				# HISTRIONICZNE ZABURZENIE OSOBOWOSCI
				'ICD10_g20', # 23				grupa 20
					'DSMIV_g21', # 24			grupa 21
				# OSOBOWOSC ZALEZNA
				'ICD10_g22', # 25				grupa 22
					'DSMIV_g23', # 26			grupa 23
				# OSOBOWOSC SCHIZOIDALNA
				'ICD10_g24', # 27				grupa 24
					'DSMIV_g25', # 28			grupa 25
				# PSYCHOPATIA
						'ICD10_148', # 29		grupa 26
						'ICD10_149', # 30		grupa 27
				'ICD10_g28', # 31				grupa 28


]

nazwy = ["",
		 "Depresja (ICD-10)", # 1
		 "Depresja (DSM-5)", # 2
		 "Anankastyczne zaburzenie osobowosci (ICD-10)", # 3
		 "Anankastyczne zaburzenie osobowosci (DSM-IV)", # 4
		 "Paranoidalne zaburzenie osobowosci (ICD-10)", # 5
		 "Paranoidalne zaburzenie osobowosci (DSM-IV)", # 6
		 "Unikowe zaburzenie osobowosci (ICD-10)", # 7
		 "Unikowe zaburzenie osobowosci (DSM-IV)",  # 8
		 "Zespol leku uogolnionego (ICD-10)", # 9
		 "Zespol leku uogolnionego (DSM-5)", # 10
		 "Zaburzenie obsesyjno-kompulsyjne (ICD-10)", # 11
		 "Histrioniczne zaburzenie osobowosci (ICD-10)", # 12
		 "Histrioniczne zaburzenie osobowosci (DSM-IV)", # 13
		 "Osobowosc zalezna (ICD-10)", # 14
		 "Osobowosc zalezna (DSM-IV)", # 15
		 "Osobowosc schizoidalna (ICD-10)", # 16
		 "Osobowosc schizoidalna (DSM-IV)", # 17
		 "Psychopatia (ICD-10)", # 18
		]

nazwy_uogolnione = [
					"Osoby zdrowe",							# 0
					"Wiecej niz jedno zaburzenie",			# 1
					"Depresja",								# 2
					"Anankastyczne zaburzenie osobowosci",	# 3
					"Paranoidalne zaburzenie osobowosci",	# 4
					"Unikowe zaburzenie osobowosci",		# 5
					"Zespol leku uogolnionego",				# 6
					"Zaburzenie obsesyjno-kompulsyjne",		# 7
					"Histrioniczne zaburzenie osobowosci",	# 8
					"Osobowosc zalezna",					# 9
					"Osobowosc schizoidalna",				# 10
					"Psychopatia",							# 11
					]

MIN_GRUPA_1_DEPRESJA_ICD10 = 2
MIN_GRUPA_2_DEPRESJA_ICD10 = 2
MIN_GRUPA_3_DEPRESJA_DSM5 = 5
MIN_GRUPA_4_ANANKASTYCZNE_ICD10 = 4
MIN_GRUPA_5_ANANKASTYCZNE_DSMIV = 5
MIN_GRUPA_6_PARANOICZNA_ICD10 = 4
MIN_GRUPA_7_PARANOICZNA_DSMIV = 4
MIN_GRUPA_8_UNIKOWE_ICD10 = 4
MIN_GRUPA_9_UNIKOWE_DSMIV = 4
MIN_GRUPA_11_ZLU_ICD10 = 1
MIN_GRUPA_12_ZLU_ICD10 = 3
MIN_GRUPA_14_ZLU_DSM5 = 3
MIN_GRUPA_18_ZOK_ICD10 = 4
MIN_GRUPA_20_HZO_ICD10 = 3
MIN_GRUPA_21_HZO_DSMIV = 5
MIN_GRUPA_22_OZ_ICD10 = 3
MIN_GRUPA_23_OZ_DSMIV = 3
MIN_GRUPA_24_OS_ICD10 = 4 # p
MIN_GRUPA_25_OS_DSMIV = 4 # p
MIN_GRUPA_28_PSYCHOPATIA_ICD10 = 4 # p

ISTNIEJACE_GRUPY = [1,2,3,0,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]

GRUPY_WYMAGAJACE_ODDZIELENIA = [1,3,4,10,13,17,20,22,24,26] # przed tymi grupami powinien byc hr

SLASH = "/"