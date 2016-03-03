from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', 'django.contrib.auth.views.login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
	# url(r'^post/(?P<pobrany_parametr>[0-9]+)/$', views.renderuj_widok_z_parametrem, name='nazwa_urla'),
	url(r'^pulpit/$', views.pulpit, name='pulpit'),
	url(r'^register/$', views.register, name='register'),
]