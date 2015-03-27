# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import deployment.validators


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0004_auto_20150325_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deployment',
            name='deployment_file',
            field=models.FileField(blank=True, null=True, upload_to=b'deployment_files', validators=[deployment.validators.validate_file_extension]),
            preserve_default=True,
        ),
    ]
