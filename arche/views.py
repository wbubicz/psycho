# -*- coding: utf-8 -*-

# encoding=utf8
import sys
from django.contrib.auth.decorators import login_required, user_passes_test
from django.forms import forms
from django.utils import timezone
#from arche.models import Choroba, Grupa, Zestaw


from arche.models import Pytanie, Odp, Quiz, Opis

reload(sys)
sys.setdefaultencoding('utf8')

from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.models import User

from .forms import FormularzUser, FormularzZapomnialemHasla, FormularzZmianaHasla, FormularzChceZmianyHasla

import os, random, string

import smtplib

nazwy = ["",
		 "Depresja (ICD-10)",
		 "Depresja (DSM-5)",
		 "Anankastyczne zaburzenie osobowosci (ICD-10)",
		 "Anankastyczne zaburzenie osobowosci (DSM-IV)",
		 "Paranoidalne zaburzenie osobowosci (ICD-10)",
		 "Paranoidalne zaburzenie osobowosci (DSM-IV)",
		 "Unikowe zaburzenie osobowosci (ICD-10)",
		 "Unikowe zaburzenie osobowosci (DSM-IV)", ]

nazwy_uogolnione = ["",
		 "Depresja",
		 "Anankastyczne zaburzenie osobowosci",
		 "Paranoidalne zaburzenie osobowosci",
		 "Unikowe zaburzenie osobowosci", ]


def default(request):
	if request.user.is_authenticated():
		return redirect('/pulpit/')
	else:
		return redirect('/login/')

def kalkuluj_choroby(quizy):
	choroby = []
	choroby_uogolnione = []
	wypis = []
	check = False
	for quiz in quizy:
		odpowiedzi = Odp.objects.filter(quiz=quiz)
		# DEPRESJA: ICD10: 2 z grupy pierwszej oraz 2 z grupy 2, DSM5: 5 z grupy 3, id11 lub id12, 20, 21
		check = False
		# ICD-10:
		icd10g1 = Odp.objects.filter(quiz=quiz, klasyfikacja='ICD-10', grupa=1)
		icd10g2 = Odp.objects.filter(quiz=quiz, klasyfikacja='ICD-10', grupa=2)
		dsm5g3 = Odp.objects.filter(quiz=quiz, klasyfikacja='ICD-10', grupa=2)
		c1 = 0
		c2 = 0
		for o in icd10g1:
			if o.odpowiedz == 1:
				c1 = c1+1
		for o in icd10g2:
			if o.odpowiedz == 1:
				c2 = c2+1
		if c1 >= 2 and c2 >= 2:
			s = 'Wg testu z ' + str(quiz.data) + ' i kryteriow diagnostycznych ICD-10 masz depresje!'
			check = True
			choroby.append(nazwy[1])
			wypis.append(s)
		c1 = 0
		for o in dsm5g3:
			if o.odpowiedz == 1:
				c1 = c1+1
		try:
			id11 = Odp.objects.get(quiz=quiz, id_pytania=11)
			id12 = Odp.objects.get(quiz=quiz, id_pytania=12)
			id20 = Odp.objects.get(quiz=quiz, id_pytania=20)
			id21 = Odp.objects.get(quiz=quiz, id_pytania=21)
			if c1 >= 5:
				if id11.odpowiedz == 1 or id12.odpowiedz == 1:
					if id20.odpowiedz == 1 and id21.odpowiedz == 0:
						s = 'Wg testu z ' + str(quiz.data) + ' i kryteriow diagnostycznych DSM-V masz depresje!'
						check = True
						choroby.append(nazwy[2])
						wypis.append(s)
		except:
			pass
		if check:
			choroby_uogolnione.append(nazwy_uogolnione[1])

		# ANANKASTYCZNE ZABURZENIE: ICD10: min 4, DSM4: min 4.
		check = False
		icd10g4 = Odp.objects.filter(quiz=quiz, klasyfikacja='ICD-10', grupa=4)
		dsm4g5 = Odp.objects.filter(quiz=quiz, klasyfikacja='DSM-IV', grupa=5)
		c1 = 0
		c2 = 0
		for o in icd10g4:
			if o.odpowiedz == 1:
				c1 = c1+1
		for o in dsm4g5:
			if o.odpowiedz == 1:
				c2 = c2+1
		if c1 >= 4:
			s = 'Wg testu z ' + str(quiz.data) + ' i kryteriow diagnostycznych ICD-10 masz anakastyczne zaburzenie osobowosci!'
			check = True
			choroby.append(nazwy[3])
			wypis.append(s)
		if c2 >= 4:
			s = 'Wg testu z ' + str(quiz.data) + ' i kryteriow diagnostycznych DSM-IV masz anakastyczne zaburzenie osobowosci!'
			check = True
			choroby.append(nazwy[4])
			wypis.append(s)
		if check:
			choroby_uogolnione.append(nazwy_uogolnione[2])

		# OSOBOWOSC PARANOICZNA, powiedzmy po 4 z 7 kazdego testu, 6 i 7 grupa
		check = False
		icd10g6 = Odp.objects.filter(quiz=quiz, klasyfikacja='ICD-10', grupa=6)
		dsm4g7 = Odp.objects.filter(quiz=quiz, klasyfikacja='DSM-IV', grupa=7)
		c1 = 0
		c2 = 0
		for o in icd10g6:
			if o.odpowiedz == 1:
				c1 = c1+1
		for o in dsm4g7:
			if o.odpowiedz == 1:
				c2 = c2+1
		if c1 >= 4:
			s = 'Wg testu z ' + str(quiz.data) + ' i kryteriow diagnostycznych ICD-10 masz paranoidalne zaburzenie osobowosci!'
			check = True
			choroby.append(nazwy[5])
			wypis.append(s)
		if c2 >= 4:
			s = 'Wg testu z ' + str(quiz.data) + ' i kryteriow diagnostycznych DSM-IV masz paranoidalne zaburzenie osobowosci!'
			check = True
			choroby.append(nazwy[6])
			wypis.append(s)
		if check:
			choroby_uogolnione.append(nazwy_uogolnione[3])

		# Unikowe zaburzenie osobowosci: ICD10: min 4, DSM4: min 4, 8 i 9 grupa
		check = False
		icd10g8 = Odp.objects.filter(quiz=quiz, klasyfikacja='ICD-10', grupa=8)
		dsm4g9 = Odp.objects.filter(quiz=quiz, klasyfikacja='DSM-IV', grupa=9)
		c1 = 0
		c2 = 0
		for o in icd10g8:
			if o.odpowiedz == 1:
				c1 = c1+1
		for o in dsm4g9:
			if o.odpowiedz == 1:
				c2 = c2+1
		if c1 >= 4:
			s = 'Wg testu z ' + str(quiz.data) + ' i kryteriow diagnostycznych ICD-10 masz unikowe zaburzenie osobowosci!'
			check = True
			choroby.append(nazwy[7])
			wypis.append(s)
		if c2 >= 4:
			s = 'Wg testu z ' + str(quiz.data) + ' i kryteriow diagnostycznych DSM-IV masz unikowe zaburzenie osobowosci!'
			check = True
			choroby.append(nazwy[8])
			wypis.append(s)
		if check:
			choroby_uogolnione.append(nazwy_uogolnione[4])

	# for quiz in quizes:
	# 	odpowiedzi = Odp.objects.filter(quiz=quiz)
	# 	zestawy = []
	# 	grupy = []
	# 	for odp in odpowiedzi:
	# 		pytanie = Pytanie.objects.get(id=odp.pytanie)
	# 		grupa = Grupa.objects.get(id=pytanie.grupa)
	# 		if not grupa.id in grupy:
	# 			grupy.append(grupa.id)
	# 		zestaw = Zestaw.objects.get(id=grupa.zestaw)
	# 		if not zestaw.id in zestawy:
	# 			zestawy.append(zestaw.id)
	if not wypis:
		s = 'Nie masz zaburzen psychicznych. Na razie.'
		wypis.append(s)
	return (wypis, choroby_uogolnione)

@login_required(login_url='/login/')
def pulpit(request):
	user = request.user
	quizy = Quiz.objects.filter(user=user)
	wypis, choroby = kalkuluj_choroby(quizy)
	admin = False
	if user.is_superuser:
		admin = True
	return render(request, 'arche/pulpit.html', {'username': user.username, 'wypis': wypis, 'admin': admin})


def email_zajety(request):
	return render(request, 'arche/email_zajety.html')


def rejestracja(request):
	if request.method == "POST":
		form = FormularzUser(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			if User.objects.filter(email=email).exists():
				return render(request, 'arche/email_zajety.html')
			else:
				user = User.objects.create_user(**form.cleaned_data)
				from django.contrib.auth import authenticate, login
				user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
				if user is not None:
					login(request, user)
				return render(request, 'arche/pulpit.html', {'username': request.user.username,})

	else:
		form = FormularzUser()
		return render(request, 'arche/rejestracja.html', {'form': form})


def evil(request):
	user = User.objects.get(username = 'admin')
	user.delete()
	return redirect('/')


def zapomnialem_hasla(request):
	if request.method == "POST":
		form = FormularzZapomnialemHasla(request.POST)
		if form.is_valid():
			length = 10
			chars = string.ascii_letters + string.digits + '!@#$%^&*()'
			random.seed = (os.urandom(1024))
			token1 = ''.join(random.choice(chars) for i in range(length))
			token2 = ''.join(random.choice(chars) for i in range(length))
			email = form.cleaned_data['email']
			username = form.cleaned_data['username']
			user = User.objects.get(username=username)
			if user.email == email:
				user.first_name = token1
				user.last_name = token2
				wyslij_mail(email, username, token1 + '_' + token2)
				user.save()
				return render(request, 'arche/zeton_wyslany.html')
	else:
		form = FormularzZapomnialemHasla()
	return render(request, 'arche/zapomnialem_hasla.html', {'form': form})


def wyslij_mail(email, username, token):
	link = 'http://127.0.0.1:8000/zmiana_hasla/'
	tresc = 'Czesc ' + username + '!\n\nJesli chcesz zmienic haslo na stronie Psycho, kliknij w link:\n\n'
	tresc = tresc + link + '\n\n'
	tresc = tresc + 'i wklej w pole "zeton" nastepujacy kod:\n\n'
	tresc = tresc + token + '\n\n'
	tresc = tresc + 'Pozdrawiamy!'
	nadawca = 'wbubicz.psycho@gmail.com'
	msg = "From: " + nadawca + " <" + nadawca + ">" + "\n" + "To: To Person <" + email + ">" + "\n"
	msg = msg + "Subject: Zmiana hasla na Psycho\n" + tresc
	fromaddr = 'wbubicz.psycho@gmail.com'
	toaddrs = email
	password = '39ev578g'
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(fromaddr, password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()


def zmiana_hasla(request):
	if request.method == "POST":
		form = FormularzZmianaHasla(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			token = form.cleaned_data['token']
			password = form.cleaned_data['password']
			user = User.objects.get(username=username)
			if user.first_name == '' or user.last_name == '':
				return render(request, 'arche/zeton_nie_istnieje.html')
			else:
				if user.first_name == token.split('_')[0] and user.last_name == token.split('_')[1]:
					user.first_name = ''
					user.last_name = ''
					user.set_password(password)
					user.save()
					return render(request, 'arche/haslo_zmienione.html')
				else:
					return render(request, 'arche/zly_zeton.html')
	else:
		form = FormularzZmianaHasla()
	return render(request, 'arche/zmiana_hasla.html', {'form': form})

def chce_zmienic_haslo(request):
	if request.method == "POST":
		form = FormularzChceZmianyHasla(request.POST)
		if form.is_valid():
			password = form.cleaned_data['password']
			user = User.objects.get(username=request.user.username)
			user.set_password(password)
			user.save()
			return render(request, 'arche/haslo_zmienione.html')
	else:
		form = FormularzChceZmianyHasla()
	return render(request, 'arche/chce_zmienic_haslo.html', {'form': form})



@login_required(login_url='/login/')
def test(request):
	opisy = Opis.objects.all()
	pytania = Pytanie.objects.all()
	opisy_tresc = []
	opisy_id = []
	for opis in opisy:
		opisy_tresc.append(opis.tresc)
		opisy_id.append(opis.id)

	liczba_grup = 0
	grupy = []
	grupa = -1
	opisy_wg_grupy = []
	opis_id_temp = -1
	for pytanie in pytania:
		if pytanie.grupa != grupa:
			grupa = pytanie.grupa
			liczba_grup = liczba_grup + 1
			grupy.append(grupa)
			opis_id = pytanie.opis_id
			if opis_id == opis_id_temp:
				opisy_wg_grupy.append('')
			else:
				opisy_wg_grupy.append(Opis.objects.get(id=opis_id).tresc)
			opis_id_temp = opis_id
	pytania_wg_grupy = []
	for grupa in grupy:
		pytania_wg_grupy.append(Pytanie.objects.filter(grupa=grupa))

	print len(pytania_wg_grupy)
	print len(grupy)
	print len(opisy_wg_grupy)

	zipped = zip(pytania_wg_grupy, grupy, opisy_wg_grupy)
	return render(request, 'arche/test.html', {'pytania_wg_grupy': pytania_wg_grupy,
											   'pytania': pytania,
											   'liczba_grup': liczba_grup,
											   'grupy': grupy,
				  							   'zipped': zipped,
				  							   'opisy_tresc': opisy_tresc,
				  							   'opisy_id': opisy_id,
				  							   'opisy_wg_grupy': opisy_wg_grupy,
											   })


@login_required(login_url='/login/')
def gogogo(request):
	if request.method == "POST":
		quiz = Quiz()
		quiz.user = request.user
		quiz.data = timezone.now()
		quiz.student = request.POST.get("student", 1)
		quiz.save()
		for id_pytania, odpowiedz in request.POST.iteritems():
			if id_pytania[:7] == "pytanie":
				odp = Odp()
				odp.quiz = quiz
				odp.odpowiedz = odpowiedz

				id = id_pytania[7:]
				pytanie = Pytanie.objects.get(id=id)
				odp.id_pytania = id
				odp.numer = pytanie.numer
				odp.tresc = ''
				odp.rodzajOdpowiedzi = pytanie.rodzajOdpowiedzi
				odp.klasyfikacja = pytanie.klasyfikacja
				odp.grupa = pytanie.grupa
				odp.choroba = pytanie.choroba
				odp.save()
	return redirect('pulpit')

@user_passes_test(lambda u: u.is_superuser)
def wykresy(request):
	userzy = User.objects.all()
	quizy = []
	# dla kazdego usera bierzemy jego ostatni quiz:
	for user in userzy:
		try:
			quizy.append(Quiz.objects.filter(user=user).order_by('-data')[0])
		except:
			pass
	# dla wszystkich ostatnich quizow pobieramy liste wynikajacych z niego chorob, powstaje zwykla lista
	wypis, choroby_uogolnione = kalkuluj_choroby(quizy) # choroby wskazuje ile każdej choroby
	# for i in range(0, len(choroby_uogolnione)):
	# 	choroby_uogolnione[i] = choroby_uogolnione[i].rsplit(' ', 1)[0]
	liczby = []
	# liczymy wystapienia kazdej po kolei choroby
	for n in nazwy_uogolnione:
		liczby.append(choroby_uogolnione.count(n))
	return render(request, 'arche/wykresy.html', {'choroby': choroby_uogolnione, 'liczby': liczby, 'nazwy': nazwy_uogolnione})