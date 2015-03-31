"""
Deployment Management
This program is designed to deploy Django code to remote locations
Copyright (C) 2015  James Fourman

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import os
from django.core.exceptions import ValidationError
from django_deployment import settings


def validate_file_extension(value):
    filename, file_extension = os.path.splitext(value.name)

    if file_extension not in settings.FILE_EXTENSION_WHITELIST:
        raise ValidationError('Not a valid archive')
