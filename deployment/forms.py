from django.forms import ModelForm
from .models import Deployment


class DeploymentForm(ModelForm):
	class Meta:
		model = Deployment
        fields = ['name', 'deployment_file', 'status', 'requester', 'creator', 'requested_date', 'create_date', 'deployment_type']