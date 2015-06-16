# -*- coding: utf-8 -*-

from django.conf import settings

__all__ = [
    'DRC_LANGUAGE',
    'DRC_MISSING_FILE_MSG',
    'DRC_EMPTY_FILE_MSG',
    'DRC_NUMBER_START',
    'DRC_NUMBER_END',
]

# setting english as the default language
DRC_LANGUAGE = getattr(settings, 'DRC_LANGUAGE', 'en')
DRC_MISSING_FILE_MSG = 'language file does not exists'
DRC_EMPTY_FILE_MSG = 'no usable lines in language file'
# random number tag limits
DRC_NUMBER_START = getattr(settings, 'DRC_NUMBER_START', 1)
DRC_NUMBER_END = getattr(settings, 'DRC_NUMBER_END', 1000)
