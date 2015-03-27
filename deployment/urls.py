from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^new_deployment/$', views.new_deployment, name='new_deployment'),
    url(r'^run_deployments/$', views.run_deployments, name='run_deployments'),
    url(r'^(?P<deployment_id>\d+)/$', views.get_deployment, name='get_deployment'),
)
