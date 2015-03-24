from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import Deployment, Status
from .forms import DeploymentForm


def index(request):
    queued = Deployment.objects.filter(status__name="queued")
    active = Deployment.objects.filter(status__name="active")
    success = Deployment.objects.filter(status__name="success")
    failed = Deployment.objects.filter(status__name="failed")

    params = {
        'queued': queued,
        'active': active,
        'success': success,
        'failed': failed
    }
    return render(request, "deployment/index.html", params)

def new_deployment(request):
    if request.method == 'POST':
        form = DeploymentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.creator = request.user
            instance.status = Status.objects.get(pk=1)
            instance = instance.save()
            return HttpResponseRedirect(reverse('deployment:index'))
    else:
        form = DeploymentForm({'requester': request.user})

    params = {
        'form': form
    }
    return render(request, "deployment/new_deployment.html", params)