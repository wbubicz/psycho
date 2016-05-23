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
					'DSM5_g5', # 8				grupa 5
				# OSOBOWOSC PARANOICZNA
				'ICD10_g6', # 9					grupa 6
					'DSM5_g7', # 10				grupa 7
				# UNIKOWE ZABURZENIE OSOBOWOSCI
				'ICD10_g8', # 11				grupa 8
					'DSM5_g9', # 12				grupa 9
				# ZESPOL LEKU UOGOLNIONEGO
						'ICD10_65', # 13		grupa 10
				'ICD10_g11', # 14				grupa 11
				'ICD10_g12', # 15				grupa 12
						'DSM5_88' # 16			grupa 13
					'DSM5_g14', # 17			grupa 14
						'DSM5_96', # 18			grupa 15
						'DSM5_97', # 19			grupa 16
				# ZABURZENIE OBSESYJNO-KOMPULSYJNE
				'ICD10_98', # 20					grupa 17
						'ICD10_g18', # 21		grupa 18
				'ICD10_103', # 22				grupa 19
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

ISTNIEJACE_GRUPY = [1,2,3,0,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

GRUPY_WYMAGAJACE_ODDZIELENIA = [1,3,4,10,13,17] # przed tymi grupami powinien byc hr

SLASH = "/"