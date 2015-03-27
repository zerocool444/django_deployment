import zipfile
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import Deployment, Status, DeploymentLog, DeploymentStep
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
        form = DeploymentForm(request.POST, request.FILES)
        if form.is_valid():
            deployment = form.save(commit=False)
            deployment.creator = request.user
            deployment.status = Status.objects.get(pk=1)
            deployment.save()
            deployment_log = DeploymentLog()
            deployment_log.deployment = deployment
            deployment_log.log_information = "Deployment has been created"
            deployment_log.source_system = "DeplomentManagement"
            deployment_log.deployment_step = DeploymentStep.objects.get(pk=1)
            deployment_log.save()
            return HttpResponseRedirect(reverse('deployment:index'))
    else:
        form = DeploymentForm({'requester': request.user})

    params = {
        'form': form
    }
    return render(request, "deployment/new_deployment.html", params)


def get_deployment(request, deployment_id):
    deployment = Deployment.objects.get(pk=deployment_id)
    deployment_logs = DeploymentLog.objects.filter(deployment_id=deployment_id)
    params = {
        'deployment': deployment,
        'deployment_logs': deployment_logs
    }
    return render(request, "deployment/get_deployment.html", params)


def run_deployments(request):
    queued = Deployment.objects.filter(status__name="queued")
    for deployment in queued:
        extension = deployment.deployment_file.name.split(".")[-1]
        name = deployment.deployment_file.name.split("/")[-1].split(".")[0]
        if extension == "zip":
            print "Running unzip on %s" % (name)
            with zipfile.ZipFile(deployment.deployment_file.path) as zf:
                zf.extractall("C:\\Users\\zerocool\\Documents\\Git\\django_deployment\\test\\" + name)
        elif extension == "tar":
            print "Running untar"
        elif extension == "gz":
            print "Running gz"

        # deployment.status = 2
        # deployment.save()

    return render(request, "deployment/deployment_started.html")
