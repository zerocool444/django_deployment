from django.db import models
from django.contrib.auth.models import User
from .validators import validate_file_extension


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
