from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.models import User

from .forms import FormularzUser


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


def rejestracja(request):
	if request.method == "POST":
		form = FormularzUser(request.POST)
		if form.is_valid():
			user = User.objects.create_user(**form.cleaned_data)
			return redirect('pulpit')
	else:
		form = FormularzUser()
	return render(request, 'arche/rejestracja.html', {'form': form})

def evil(request):
	# user = User.objects.get(username = 'aaaa')
	# user.delete()
	user = User.objects.get(username = 'user1')
	user.delete()
	user = User.objects.get(username = 'user188')
	user.delete()
	user = User.objects.get(username = 'asfas')
	user.delete()
# user1
# user188
# asfas
	return redirect('/')