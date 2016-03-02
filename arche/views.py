from django.shortcuts import render, get_object_or_404, redirect

def logowanie(request):
	return render(request, 'arche/logowanie.html', {})