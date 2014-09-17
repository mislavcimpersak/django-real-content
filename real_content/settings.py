# -*- coding: utf-8 -*-

from django.conf import settings

# setting english as the default language
DRC_LANGUAGE = getattr(settings, 'DRC_LANGUAGE', 'en')
