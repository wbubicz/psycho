from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


def pulpit(request):
	return render(request, 'arche/pulpit.html', {})


def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/pulpit/")
	else:
		form = UserCreationForm()
	return render(request, "registration/register.html", {'form': form,})