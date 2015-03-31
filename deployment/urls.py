"""
Deployment Management
This program is designed to deploy Django code to remote locations
Copyright (C) 2015  James Fourman

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^new_deployment/$', views.new_deployment, name='new_deployment'),
    url(r'^run_deployments/$', views.run_deployments, name='run_deployments'),
    url(r'^(?P<deployment_id>\d+)/$', views.get_deployment, name='get_deployment'),
)
