# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0002_auto_20150321_2157'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'Status'},
        ),
        migrations.AlterField(
            model_name='deployment',
            name='deployment_file',
            field=models.FileField(null=True, upload_to=b''),
            preserve_default=True,
        ),
    ]
