# -*- coding: utf-8 -*-
# encoding=utf8

import sys
import os, random, string
import smtplib
import time, datetime
import collections
from random import randint
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from arche.backend.kalkulacja_chorob import kalkuluj_choroby
from arche.models import Pytanie, Odp, Quiz, Opis
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import FormularzUser, FormularzZapomnialemHasla, FormularzZmianaHasla, FormularzChceZmianyHasla
from arche.backend.stale import *
from django.contrib.auth import authenticate, login

reload(sys)
sys.setdefaultencoding('utf8')


def default(request):
	if request.user.is_authenticated():
		return redirect('/pulpit/')
	else:
		return redirect('/login/')


@login_required(login_url='/login/')
def pulpit(request):
	czas_start = time.time()
	user = request.user
	quizy = Quiz.objects.filter(user=user)
	wypis_python, choroby_uogolnione, wypis_datalog, czas_python, czas_datalog = kalkuluj_choroby(quizy)
	wypis_python = collections.OrderedDict(sorted(wypis_python.items()))
	wypis_datalog = collections.OrderedDict(sorted(wypis_datalog.items()))

	wypis1, wypis2, wypis3 = [], [], []
	temp = ''
	for x in wypis_python:
		wypis_python[x] = collections.OrderedDict(sorted(wypis_python[x].items()))
		for y in wypis_python[x]:
			if x == temp:
				wypis1.append("")
			else:
				wypis1.append("Test z " + str(x)[:-15])
				temp = x
			wypis2.append(y + ":")
			wypis3.append(wypis_python[x][y])
	wypis_python_zipped = zip(wypis1, wypis2, wypis3)

	wypis1, wypis2, wypis3 = [], [], []
	temp = ''
	for x in wypis_datalog:
		wypis_datalog[x] = collections.OrderedDict(sorted(wypis_datalog[x].items()))
		for y in wypis_datalog[x]:
			if x == temp:
				wypis1.append("")
			else:
				wypis1.append("Test z " + str(x)[:-15])
				temp = x
			wypis2.append(y + ":")
			wypis3.append(wypis_datalog[x][y])
	wypis_datalog_zipped = zip(wypis1, wypis2, wypis3)

	admin = False
	if user.is_superuser:
		admin = True
	czas_koniec = time.time()
	czas_wykonania = czas_koniec - czas_start

	wypis_python_html = collections.OrderedDict()
	for q in wypis_python:
		wypis_python_html[q] = collections.OrderedDict()
		wypis_python_html[q][nazwy_uogolnione_s[0]] = [ str( wypis_python[q][nazwy[3]] ), str( wypis_python[q][nazwy[4]] ) ]
		wypis_python_html[q][nazwy_uogolnione_s[1]] = [ str( wypis_python[q][nazwy[1]] ), str( wypis_python[q][nazwy[2]] ) ]
		wypis_python_html[q][nazwy_uogolnione_s[2]] = [ str( wypis_python[q][nazwy[12]] ), str( wypis_python[q][nazwy[13]] ) ]
		wypis_python_html[q][nazwy_uogolnione_s[3]] = [ str( wypis_python[q][nazwy[16]] ), str( wypis_python[q][nazwy[17]] ) ]
		wypis_python_html[q][nazwy_uogolnione_s[4]] = [ str( wypis_python[q][nazwy[14]] ), str( wypis_python[q][nazwy[15]] ) ]
		wypis_python_html[q][nazwy_uogolnione_s[5]] = [ str( wypis_python[q][nazwy[5]] ), str( wypis_python[q][nazwy[6]] ) ]
		wypis_python_html[q][nazwy_uogolnione_s[6]] = [ str( wypis_python[q][nazwy[11]] ), 'bd' ]
		wypis_python_html[q][nazwy_uogolnione_s[7]] = [ str( wypis_python[q][nazwy[7]] ), str( wypis_python[q][nazwy[8]] ) ]
		wypis_python_html[q][nazwy_uogolnione_s[8]] = [ str( wypis_python[q][nazwy[18]] ), 'bd' ]
		wypis_python_html[q][nazwy_uogolnione_s[9]] = [ str( wypis_python[q][nazwy[9]] ), str( wypis_python[q][nazwy[10]] ) ]

	wypis_datalog_html = collections.OrderedDict()
	for q in wypis_datalog:
		wypis_datalog_html[q] = collections.OrderedDict()
		wypis_datalog_html[q][nazwy_uogolnione_s[0]] = [ str( wypis_datalog[q][nazwy[3]] ), str( wypis_datalog[q][nazwy[4]] ) ]
		wypis_datalog_html[q][nazwy_uogolnione_s[1]] = [ str( wypis_datalog[q][nazwy[1]] ), str( wypis_datalog[q][nazwy[2]] ) ]
		wypis_datalog_html[q][nazwy_uogolnione_s[2]] = [ str( wypis_datalog[q][nazwy[12]] ), str( wypis_datalog[q][nazwy[13]] ) ]
		wypis_datalog_html[q][nazwy_uogolnione_s[3]] = [ str( wypis_datalog[q][nazwy[16]] ), str( wypis_datalog[q][nazwy[17]] ) ]
		wypis_datalog_html[q][nazwy_uogolnione_s[4]] = [ str( wypis_datalog[q][nazwy[14]] ), str( wypis_datalog[q][nazwy[15]] ) ]
		wypis_datalog_html[q][nazwy_uogolnione_s[5]] = [ str( wypis_datalog[q][nazwy[5]] ), str( wypis_datalog[q][nazwy[6]] ) ]
		wypis_datalog_html[q][nazwy_uogolnione_s[6]] = [ str( wypis_datalog[q][nazwy[11]] ), 'bd' ]
		wypis_datalog_html[q][nazwy_uogolnione_s[7]] = [ str( wypis_datalog[q][nazwy[7]] ), str( wypis_datalog[q][nazwy[8]] ) ]
		wypis_datalog_html[q][nazwy_uogolnione_s[8]] = [ str( wypis_datalog[q][nazwy[18]] ), 'bd' ]
		wypis_datalog_html[q][nazwy_uogolnione_s[9]] = [ str( wypis_datalog[q][nazwy[9]] ), str( wypis_datalog[q][nazwy[10]] ) ]

	tabelki_python = []
	naglowki_python = []
	for q in wypis_python_html:
		s = ""
		s = s + '<table class="w3-table"> <tr class="w3-blue"> <th>Test z ' + str(q)[:-9] + '</th>'
		s = s + '<th class="w3-center">ICD-10</th><th class="w3-center">DSM-IV</th></tr>'
		naglowki_python.append('Test z ' + str(q)[:-9])
		for choroba in wypis_python_html[q]:
			s = s + '<tr class="w3-white">'
			s = s + '<td>' + choroba + '</td>'
			for wynik in wypis_python_html[q][choroba]:
				if wynik == 'True':
					s = s + '<td class="w3-green w3-center">' + '&#10004;' + '</td>'
				else:
					s = s + '<td class="w3-center">' + '&#10007;' + '</td>'
			s = s + '</tr>'
		s = s + '</table>'
		tabelki_python.append(s)
	quizy_python_zipped = zip(naglowki_python, tabelki_python)

	tabelki_datalog = []
	naglowki_datalog = []
	for q in wypis_python_html:
		s = ""
		s = s + '<table class="w3-table"> <tr class="w3-blue"> <th>Test z ' + str(q)[:-9] + '</th>'
		s = s + '<th class="w3-center">ICD-10</th><th class="w3-center">DSM-IV</th></tr>'
		naglowki_datalog.append('Test z ' + str(q)[:-9])
		for choroba in wypis_python_html[q]:
			s = s + '<tr class="w3-white">'
			s = s + '<td>' + choroba + '</td>'
			for wynik in wypis_python_html[q][choroba]:
				if wynik == 'True':
					s = s + '<td class="w3-green w3-center">' + '&#10004;' + '</td>'
				else:
					s = s + '<td class="w3-center">' + '&#10007;' + '</td>'
			s = s + '</tr>'
		s = s + '</table>'
		tabelki_datalog.append(s)
	quizy_datalog_zipped = zip(naglowki_python, tabelki_datalog)

	return render(request, 'arche/pulpit.html', {'username': user.username,
												 'wypis_python_zipped': wypis_python_zipped,
												 'wypis_datalog_zipped': wypis_datalog_zipped,
												 'czas_python': czas_python,
												 'czas_datalog': czas_datalog,
												 'czas_wykonania': czas_wykonania,
												 'wypis_datalog': wypis_datalog,
												 'quizy_python_zipped': quizy_python_zipped,
												 'quizy_datalog_zipped': quizy_datalog_zipped,
												 'admin': admin})


def email_zajety(request):
	return render(request, 'arche/email_zajety.html')


def rejestracja(request):
	if request.method == "POST":
		form = FormularzUser(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			username=form.cleaned_data['username']
			if User.objects.filter(email=email).exists():
				return render(request, 'arche/email_zajety.html')
			if User.objects.filter(username=username).exists():
				return render(request, 'arche/email_zajety.html')
			else:
				user = User.objects.create_user(**form.cleaned_data) # to jest potrzebne
				user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
				if user is not None:
					login(request, user)
				return render(request, 'arche/pulpit.html', {'username': request.user.username,})

	else:
		form = FormularzUser()
	return render(request, 'arche/rejestracja.html', {'form': form})


def evil(request):
	user = User.objects.get(username='admin')
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
	link = 'http://wbubicz.pythonanywhere.com/zmiana_hasla/'
	tresc = u'Cześć ' + username + u'!\n\nJeśli chcesz zmienić hasło na stronie Psycho, kliknij w link:\n\n'
	tresc = tresc + link + '\n\n'
	tresc = tresc + u'i wklej w pole "token" następujacy kod:\n\n'
	tresc = tresc + token + '\n\n'
	tresc = tresc + 'Pozdrawiamy!'
	nadawca = 'wbubicz.psycho@gmail.com'
	msg = "From: " + nadawca + " <" + nadawca + ">" + "\n" + "To: To Person <" + email + ">" + "\n"
	msg = msg + u"Subject: Zmiana hasła na Psycho\n" + tresc
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
	pytania = Pytanie.objects.all()
	pytania_wg_grupy, opisy_wg_grupy = [], []
	grupy = []
	hr = []
	for i in ISTNIEJACE_GRUPY: # przepisanie list bo jest TEN motyw
		grupy.append(i)
		hr.append(i)
	for grupa in grupy:
		pytania_wg_grupy.append(Pytanie.objects.filter(grupa=grupa))
	opis_id_temp = -1 # do sprawdzania czy opis sie powtarza
	for pwg in pytania_wg_grupy:
		opis_id = pwg[0].opis_id # bierzemy pierwsze pytanie z grupy i sprawdzamy opis
		if opis_id == opis_id_temp:
			opisy_wg_grupy.append('')
		else:
			opisy_wg_grupy.append(Opis.objects.get(id=opis_id).tresc)
		opis_id_temp = opis_id
	for i in range(len(hr)):
		if hr[i] in GRUPY_WYMAGAJACE_ODDZIELENIA:
			hr[i] = True
		else:
			hr[i] = False

	zipped = zip(pytania_wg_grupy, grupy, opisy_wg_grupy, hr)

	wieki = range(15,91)
	return render(request, 'arche/test.html', {'zipped': zipped, 'wieki': wieki})


@login_required(login_url='/login/')
def gogogo(request):
	if request.method == "POST":
		quiz = Quiz()
		quiz.user = request.user
		quiz.data = timezone.now()
		quiz.student = request.POST.get("student", 1)
		quiz.plec = request.POST.get("plec", "M")
		quiz.wiek = request.POST.get("wiek", 18)
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
	# choroby_uogolnione zawiera liczbe chorob z kazdego typu
	wypis_python, choroby_uogolnione, wypis_datalog, czas_python, czas_datalog  = kalkuluj_choroby(quizy)
	liczby = []
	# liczymy wystapienia kazdej po kolei choroby
	for n in nazwy_uogolnione:
		liczby.append(choroby_uogolnione.count(n))
	wiek = [0]*100
	for q in quizy:
		wiek[q.wiek] = wiek[q.wiek] + 1
	wieki = []
	liczby_wiekow = []
	for i in range(0,100):
		if wiek[i] > 0:
			wieki.append(str(i))
			liczby_wiekow.append(wiek[i])
	return render(request, 'arche/wykresy.html', {
													'choroby': choroby_uogolnione,
													'liczby': liczby,
													'nazwy': nazwy_uogolnione,
													'wieki': wieki,
													'liczby_wiekow': liczby_wiekow,
												})


def load(request):
	for i in range(200):
		length = 5
		chars = string.ascii_letters
		random.seed = (os.urandom(1024))
		username = ''.join(random.choice(chars) for i in range(length)).lower()
		email = username + '@' + ''.join(random.choice(chars) for i in range(3)).lower() + '.pl'
		# password = ''.join(random.choice(chars) for i in range(8))
		password = 'alalalal'
		user = User.objects.create_user(username, email, password)
		user.last_login = losuj_date_z_przedzialu("5/31/2016 5:00 PM", "6/30/2016 5:00 PM", '%m/%d/%Y %I:%M %p')
		user.save()
		student = randint(0, 6)
		quiz = Quiz()
		quiz.user = user
		quiz.data = losuj_date()
		quiz.student = student
		quiz.save()
		pytania = Pytanie.objects.all()
		for p in pytania:
			odp = Odp()
			odp.quiz = quiz
			if randint(1, 10) > 7:
				odp.odpowiedz = 1
			else:
				odp.odpowiedz = 0
			odp.id_pytania = p.id
			odp.numer = p.numer
			odp.tresc = ''
			odp.rodzajOdpowiedzi = p.rodzajOdpowiedzi
			odp.klasyfikacja = p.klasyfikacja
			odp.grupa = p.grupa
			odp.choroba = p.choroba
			odp.save()
		# from django.contrib.auth import authenticate, login
		# user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
		# if user is not None:
		# 	login(request, user)
	return redirect('/')


def losuj_date_z_przedzialu(poczatek, koniec, format):
	poczatek_w_ms = time.mktime(time.strptime(poczatek, format))
	koniec_w_ms = time.mktime(time.strptime(koniec, format))
	print poczatek_w_ms
	print koniec_w_ms
	wybrany_czas_w_ms = poczatek_w_ms + random.random() * (koniec_w_ms - poczatek_w_ms)
	wybrany_czas_w_ms = round(wybrany_czas_w_ms, 3)
	print wybrany_czas_w_ms
	# print datetime.strptime('%Y-%m-%d %H:%M:%S.%f', time.localtime(wybrany_czas_w_ms))
	# return datetime.strptime('%Y-%m-%d %H:%M:%S.%f', time.localtime(wybrany_czas_w_ms))
	print datetime.datetime.fromtimestamp(wybrany_czas_w_ms)
	return datetime.datetime.fromtimestamp(
		wybrany_czas_w_ms)  # ('%Y-%m-%d %H:%M:%S.%f', time.localtime(wybrany_czas_w_ms))


def losuj_date():
	return losuj_date_z_przedzialu("4/1/2016 11:00 AM", "5/31/2016 5:00 PM", '%m/%d/%Y %I:%M %p')