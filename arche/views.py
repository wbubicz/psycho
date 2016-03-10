# -*- coding: utf-8 -*-

# encoding=utf8
import sys

from django.contrib.auth.hashers import make_password
from django.forms import forms

reload(sys)
sys.setdefaultencoding('utf8')

from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.models import User

from .forms import FormularzUser, FormularzZapomnialemHasla, FormularzZmianaHasla

import os, random, string

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText


def default(request):
	if request.user.is_authenticated():
		return redirect('/pulpit/')
	else:
		return redirect('/login/')


def pulpit(request):
	return render(request, 'arche/pulpit.html', {'username': request.user.username,})


# def login(request):
# 	if request.method == "POST":
# 		username = request.POST.get('username', '')
# 		password = request.POST.get('password', '')
# 		user = User.objects.authenticate(username = username, password = password)
# 		if user is not None:
# 			auth.login(request, user)
# 			return HttpResponseRedirect(reverse('home'))
# 		else:
# 			return HttpResponseRedirect('/accounts/invalid')
# 	return render(request, 'arche/login.html')

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
	# user = User.objects.get(username = 'aaaa')
	# user.delete()
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
	# tresc = 'Cześć ' + username + '!\n\nJeśli chcesz zmienić hasło na stronie Psycho, kliknij w link:\n\n'
	# tresc = tresc + link + '\n\n'
	# tresc = tresc + 'i wklej w pole "żeton" następujący kod:\n\n'
	# tresc = tresc + token + '\n\n'
	# tresc = tresc + 'Pozdrawiamy!'

	tresc = 'Czesc ' + username + '!\n\nJesli chcesz zmienic haslo na stronie Psycho, kliknij w link:\n\n'
	tresc = tresc + link + '\n\n'
	tresc = tresc + 'i wklej w pole "zeton" nastepujacy kod:\n\n'
	tresc = tresc + token + '\n\n'
	tresc = tresc + 'Pozdrawiamy!'

	# msg = MIMEText(tresc)
	#
	# # me == the sender's email address
	# # you == the recipient's email address
	# #msg['Subject'] = 'Zmiana hasła na Psycho'
	# msg['Subject'] = 'Zmiana hasla na Psycho'
	# msg['From'] = 'wbubicz.psycho@gmail.com'
	# msg['To'] = email

	nadawca = 'wbubicz.psycho@gmail.com'

	msg = "From: " + nadawca + " <" + nadawca + ">" + "\n" + "To: To Person <" + email + ">" + "\n"
	msg = msg + "Subject: Zmiana hasla na Psycho\n" + tresc

	# s = smtplib.SMTP('localhost')
	# s.sendmail(me, [you], msg.as_string())
	# s.quit()

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