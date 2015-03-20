# django_deployment
This repository will store a version of Django that will offer a user interface approach to deploying code automatically.  This is largely going to be focused on using Linux as the host.

# Settings Local File
## settings_local.py

```python
Settings:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
    }
}

SECRET_KEY = '' # 50 character string

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
```