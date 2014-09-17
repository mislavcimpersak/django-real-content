# -*- coding: utf-8 -*-

from optparse import make_option

from django.core.management import BaseCommand

from real_content.models import Language, Content

"""
python manage.py drc_loaddata -d titles_hr -l hr -c title
python manage.py drc_loaddata -d titles_en -l en -c title
python manage.py drc_loaddata -d paragraphs_hr -l hr -c paragraph
python manage.py drc_loaddata -d paragraphs_en -l en -c paragraph
"""

class Command(BaseCommand):
    help = u""" go """
    option_list = BaseCommand.option_list + (
        make_option('-d', '--doc', action='store', dest='doc',
            help=u'file to parse'),
        make_option('-l', '--language', action='store', dest='language',
            help=u'language of url'),
        make_option('-c', '--cat', action='store', dest='cat',
            help=u'category of content'),
        )

    def handle(self, *args, **options):
        doc = options.get('doc', None)
        
        language = options.get('language', '')
        language = Language.get_languages(language, single=True)
        
        cat = options.get('cat', 'paragraph')
        category = getattr(Content.CONTENT_CATEGORY, cat)

        if doc:
            for line in open(doc, 'r').readlines():
                content, created = Content.objects.get_or_create(
                    content=line,
                    defaults={
                        'language': language,
                        'source': u'http://{0}.wikipedia.org'.format(language.short[:2]),
                        'content_category': category
                        }
                    )
