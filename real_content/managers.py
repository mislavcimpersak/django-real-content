# -*- coding: utf-8 -*-

from django.db import models


class RandomManager(models.Manager):
    """
    Not really optimized, but then again, it's just for dev purposes.
    """
    def get_query_set(self):
        return super(RandomManager, self).get_query_set().order_by('?')
