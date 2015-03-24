# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Deployment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('deployment_file', models.FileField(upload_to=b'')),
                ('requested_date', models.DateTimeField(auto_now_add=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(related_name='creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeploymentConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_num', models.IntegerField()),
                ('script_file', models.FileField(upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeploymentConfigurationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeploymentLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('log_information', models.TextField()),
                ('source_system', models.CharField(max_length=200, null=True)),
                ('deployment', models.ForeignKey(to='deployment.Deployment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeploymentStep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeploymentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='deploymentlog',
            name='deployment_step',
            field=models.ForeignKey(to='deployment.DeploymentStep'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deploymentconfiguration',
            name='configuration_type',
            field=models.ForeignKey(to='deployment.DeploymentConfigurationType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deploymentconfiguration',
            name='deployment',
            field=models.ForeignKey(to='deployment.Deployment'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='deploymentconfiguration',
            unique_together=set([('deployment', 'configuration_type')]),
        ),
        migrations.AddField(
            model_name='deployment',
            name='deployment_type',
            field=models.ForeignKey(to='deployment.DeploymentType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deployment',
            name='requester',
            field=models.ForeignKey(related_name='requester', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deployment',
            name='status',
            field=models.ForeignKey(to='deployment.Status'),
            preserve_default=True,
        ),
    ]
