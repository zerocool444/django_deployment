# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deploymentconfiguration',
            name='configuration_type',
            field=models.ForeignKey(to='deployment.DeploymentType'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='DeploymentConfigurationType',
        ),
    ]
