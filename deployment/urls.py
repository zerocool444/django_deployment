from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^new_deployment/$', views.new_deployment, name='new_deployment'),
)
