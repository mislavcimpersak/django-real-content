# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import RandomManager
from .choices import Choices


class Language(models.Model):
    u"""
    Langauge model storing basic language info.
    """
    short = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=150)
    
    objects = models.Manager() # The default manager.
    randoms = RandomManager() # The random-specific manager.

    class Meta:
        ordering = ('short', )

    def __unicode__(self):
        return self.name

    @staticmethod
    def get_languages(lang, single=False):
        u"""
        Used to determine which language instance should be used.
        """
        if lang:
            if isinstance(lang, Language):
                languages = [lang]
            else:
                lang = lang.lower()
                if len(lang) == 2:
                    try:
                        languages = Language.objects.filter(short__startswith=lang)
                    except Language.DoesNotExist:
                        languages = []
                elif len(lang) == 5:
                    try:
                        languages = [Language.objects.get(short=lang)]
                    except Language.DoesNotExist:
                        languages = []
                else:
                    languages = []
        else:
            languages = Language.get_languages(settings.DRC_LANGUAGE)
        if single:
            return languages[0]
        else:
            return languages


class Content(models.Model):
    u"""
    Main model holding paragraphs and titles for display on frontend.
    """
    CONTENT_CATEGORY = Choices(
        ('p', 'paragraph', _(u'Paragraph')),
        ('t', 'title', _(u'Title')),
    )

    language = models.ForeignKey(Language)
    content = models.TextField(unique=True)
    content_category = models.CharField(max_length=1, choices=CONTENT_CATEGORY,
        default=CONTENT_CATEGORY.paragraph)
    source = models.URLField(blank=True, default='')
    active = models.BooleanField(default=True)
    length = models.PositiveIntegerField(default=0)

    objects = models.Manager()
    randoms = RandomManager()

    def __unicode__(self):
        return self.content_short

    def save(self, *args, **kwargs):
        u"""
        Writing content length on model save.
        """
        self.length = len(self.content)
        super(Content, self).save(*args, **kwargs)

    @property
    def content_short(self):
        u"""
        Used as a ahorter representation of what the instance holds.
        """
        if len(self.content) > 50:
            return u'{0}{1}'.format(self.content[:50], '...')
        else:
            return u'{0}'.format(self.content)
