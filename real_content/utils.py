# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

from .models import Language, Content


def save_content(content, tag, category='paragraph', url='', language='',
    min_length=150):
    
    category = getattr(Content.CONTENT_CATEGORY, category)
    for tag in content.find_all(tag):
        new_content = ' '.join(
                [part.strip() for part in tag.getText().split('\n')]
            ).strip()
        
        if len(new_content) > min_length:
            # try to create new object, if it already exists, it passes
            content, created = Content.objects.get_or_create(
                content=new_content,
                defaults={
                    'language': language,
                    'source': url,
                    'content_category': category
                    }
                )


def parse_url(url, language=''):
    language = Language.get_languages(language, single=True)
    try:
        soup = BeautifulSoup(urllib2.urlopen(url).read())

        # saving paragraphs
        save_content(soup, 'p', 'paragraph', url=url, language=language,
            min_length=150)

        # saving all headings
        for i in range(1, 7):
            heading_level = 'h{0}'.format(i)
            save_content(soup, heading_level, 'title', url=url, language=language,
                min_length=20)
        return 'success!'
    
    except urllib2.HTTPError:
        return '403 error'
