from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.models import User


# from arche.models import MojUserCreationForm


def default(request):
	if request.user.is_authenticated():
		return redirect('/pulpit/')
	else:
		return redirect('/accounts/login/')


def pulpit(request):
	# user = User.objects.create_user('john2', '', 'johnpassword')
	# user.last_name = 'Lennon'
	# user.save()
	u = get_object_or_404(User, username='john')
	return render(request, 'arche/pulpit.html', {'u': u,})


	# def register(request):
	# 	if request.method == 'POST':
	# 		form = UserCreationForm(request.POST)
	# 		if form.is_valid():
	# 			new_user = form.save()
	# 			return HttpResponseRedirect("/pulpit/")
	# 	else:
	# 		form = UserCreationForm()
	# 	return render(request, "registration/register.html", {'form': form,})


	# def register(request):
	# 	form = MojUserCreationForm()
	# 	return render(request, 'registration/registration_form.html', {'form': form})