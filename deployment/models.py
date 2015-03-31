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
from django.db import models
from django.contrib.auth.models import User
from .validators import validate_file_extension


class Server(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


class Status(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Status'

    def __str__(self):
        return self.name


class DeploymentType(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Deployment(models.Model):
    name = models.CharField(max_length=200)
    deployment_file = models.FileField(null=True, blank=True, upload_to='deployment_files', validators=[validate_file_extension])
    status = models.ForeignKey(Status, editable=False)
    requester = models.ForeignKey(User, related_name='requester')
    creator = models.ForeignKey(User, related_name='creator', editable=False)
    requested_date = models.DateTimeField(auto_now_add=True)
    create_date = models.DateTimeField(auto_now_add=True)
    deployment_type = models.ForeignKey(DeploymentType)

    def __str__(self):
        return self.name


class DeploymentStep(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class DeploymentLog(models.Model):
    deployment = models.ForeignKey(Deployment)
    timestamp = models.DateTimeField(auto_now=True)
    log_information = models.TextField()
    source_system = models.CharField(max_length=200, null=True)
    deployment_step = models.ForeignKey(DeploymentStep)

    def __str__(self):
        return self.deployment.name


class DeploymentConfiguration(models.Model):
    deployment = models.ForeignKey(Deployment)
    configuration_type = models.ForeignKey(DeploymentType)
    order_num = models.IntegerField()
    script_file = models.FileField()

    class Meta:
        unique_together = ('deployment', 'configuration_type')

    def __str__(self):
        return self.deployment


class SettingType(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Setting(models.Model):
    deployment_type = models.ForeignKey(DeploymentType)
    setting_type = models.ForeignKey(SettingType)
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ':' + self.value
