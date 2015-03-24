from django.contrib import admin
from .models import Status, DeploymentType, Deployment, DeploymentStep, DeploymentLog, DeploymentConfiguration

admin.site.register(Status)
admin.site.register(DeploymentType)
admin.site.register(Deployment)
admin.site.register(DeploymentStep)
admin.site.register(DeploymentLog)
admin.site.register(DeploymentConfiguration)
