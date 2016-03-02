from django.shortcuts import render, get_object_or_404, redirect

def pulpit(request):
	return render(request, 'arche/pulpit.html', {})