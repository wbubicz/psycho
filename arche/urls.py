from django.conf.urls import url, include
from . import views

# from registration.forms import RegistrationFormUniqueEmail

urlpatterns = [
	url(r'^$', views.default, name='default'),
	# url(r'^accounts/register', views.register, name='register'),
	# url(r'^post/(?P<pobrany_parametr>[0-9]+)/$', views.renderuj_widok_z_parametrem, name='nazwa_urla'),
	url(r'^pulpit/$', views.pulpit, name='pulpit'),

	# url(r'^accounts/register/$', 'registration.views.register',
	# 	{'form_class': RegistrationFormUniqueEmail,
	# 	 'backend': 'registration.backends.default.DefaultBackend'},
	# 	name='registration_register'),
]