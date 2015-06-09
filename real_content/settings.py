# -*- coding: utf-8 -*-

from django.conf import settings

__all__ = [
    "DRC_LANGUAGE",
]

# setting english as the default language
DRC_LANGUAGE = getattr(settings, 'DRC_LANGUAGE', 'en')
