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
from django.contrib import admin
from .models import Status, DeploymentType, Deployment, DeploymentStep, DeploymentLog, DeploymentConfiguration, Setting, SettingType


admin.site.register(Status)
admin.site.register(DeploymentType)
admin.site.register(Deployment)
admin.site.register(DeploymentStep)
admin.site.register(DeploymentLog)
admin.site.register(DeploymentConfiguration)
admin.site.register(Setting)
admin.site.register(SettingType)
