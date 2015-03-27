import os
from django.core.exceptions import ValidationError
from django_deployment import settings


def validate_file_extension(value):
    filename, file_extension = os.path.splitext(value.name)

    if file_extension not in settings.FILE_EXTENSION_WHITELIST:
        raise ValidationError('Not a valid archive')
