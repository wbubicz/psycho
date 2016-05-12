# -*- coding: utf-8 -*-
# encoding=utf8

nazwy_grup = [
				# DEPRESJA
				'ICD10_g1', # 0
				'ICD10_g2', # 1
					'DSM5_g3', # 2
						'DSM5_11', # 3
						'DSM5_12', # 4
						'DSM5_20', # 5
						'DSM5_21', # 6
				# ANANKASTYCZNE ZABURZENIE
				'ICD10_g4', # 7
					'DSM5_g5', # 8
				# OSOBOWOSC PARANOICZNA
				'ICD10_g6', # 9
					'DSM5_g7', # 10
				# UNIKOWE ZABURZENIE OSOBOWOSCI
				'ICD10_g8', # 11
					'DSM5_g9', # 12
				# #
				# 'ICD10_g', # 13
				# 	'DSM5_g', # 14
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
		]

nazwy_uogolnione = ["Osoby zdrowe",
		 "Depresja",
		 "Anankastyczne zaburzenie osobowosci",
		 "Paranoidalne zaburzenie osobowosci",
		 "Unikowe zaburzenie osobowosci",
		 "Wiecej niz jedno zaburzenie", ]

MIN_GRUPA_1_DEPRESJA_ICD10 = 2
MIN_GRUPA_2_DEPRESJA_ICD10 = 2
MIN_GRUPA_3_DEPRESJA_DSM5 = 5
MIN_GRUPA_4_ANANKASTYCZNE_ICD10 = 4
MIN_GRUPA_5_ANANKASTYCZNE_DSMIV = 5
MIN_GRUPA_6_PARANOICZNA_ICD10 = 4
MIN_GRUPA_7_PARANOICZNA_DSMIV = 4
MIN_GRUPA_8_UNIKOWE_ICD10 = 4
MIN_GRUPA_9_UNIKOWE_DSMIV = 4