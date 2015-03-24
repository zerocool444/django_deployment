from django.forms import ModelForm
from .models import Deployment


class DeploymentForm(ModelForm):
	class Meta:
		model = Deployment
