# -*- coding: utf-8 -*-

from django.conf import settings

__all__ = [
    'DRC_LANGUAGE',
    'DRC_MISSING_FILE_MSG',
    'DRC_EMPTY_FILE_MSG',
]

# setting english as the default language
DRC_LANGUAGE = getattr(settings, 'DRC_LANGUAGE', 'en')
DRC_MISSING_FILE_MSG = 'language file does not exists'
DRC_EMPTY_FILE_MSG = 'no usable lines in language file'
