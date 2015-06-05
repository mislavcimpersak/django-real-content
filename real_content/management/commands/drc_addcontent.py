# -*- coding: utf-8 -*-

from optparse import make_option

from django.core.management import BaseCommand

from real_content.drc_utils import parse_url


class Command(BaseCommand):
    help = u"""
        Collect titles and paragraphs from given url.
        If no language is provided, it will use the one given in settings.

        Example:
        ./manage.py drc_addcontent -u http://www.24sata.hr/a-383985 -l hr
        """

    option_list = BaseCommand.option_list + (
        make_option('-u', '--url', action='store', dest='url',
            help=u'url to parse'),
        make_option('-l', '--language', action='store', dest='language',
            help=u'language of url'),
        )

    def handle(self, *args, **options):
        url = options.get('url', None)
        language = options.get('language', '')

        if url:
            parse_url(url, language)
        else:
            print('Enter url using "-u" option')
