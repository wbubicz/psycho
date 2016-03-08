from django.conf.urls import url, include
from . import views

# from registration.forms import RegistrationFormUniqueEmail

urlpatterns = [
	url(r'^$', views.default, name='default'),
	# url(r'^post/(?P<pobrany_parametr>[0-9]+)/$', views.renderuj_widok_z_parametrem, name='nazwa_urla'),
	url(r'^pulpit/$', views.pulpit, name='pulpit'),
	url(r'^evil/$', views.evil, name='evil'),
	#url(r'^login/$', views.login, name='login'),
	url(r'^rejestracja/$', views.rejestracja, name='rejestracja'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
	url(r'^login/$', 'django.contrib.auth.views.login'),
]