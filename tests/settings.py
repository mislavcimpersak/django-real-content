# -*- coding: utf-8 -*-

SECRET_KEY = 'dummy'

INSTALLED_APPS = (
    'real_content',
    'tests',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}
