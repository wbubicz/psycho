from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', 'django.contrib.auth.views.login'),
]