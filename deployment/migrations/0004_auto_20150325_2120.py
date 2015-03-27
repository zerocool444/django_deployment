# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import deployment.validators


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0003_auto_20150321_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deployment',
            name='creator',
            field=models.ForeignKey(related_name='creator', editable=False, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deployment',
            name='deployment_file',
            field=models.FileField(null=True, upload_to=b'deployment_files', validators=[deployment.validators.validate_file_extension]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deployment',
            name='status',
            field=models.ForeignKey(editable=False, to='deployment.Status'),
            preserve_default=True,
        ),
    ]
