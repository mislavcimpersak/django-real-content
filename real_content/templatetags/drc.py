# -*- coding: utf-8 -*-

import random

from django import template

from real_content.drc_utils import get_language, get_text_file
from real_content.settings import DRC_MISSING_FILE_MSG, DRC_EMPTY_FILE_MSG

register = template.Library()


def random_lines(text_file, no_of_lines=1):
    u"""
    Gets a random line from a file ignoring lines starting with # and empty
    lines.
    """
    if text_file is None:
        return DRC_MISSING_FILE_MSG
    lines = text_file.read().splitlines()
    clean_lines = [line for line in lines
        if line.startswith('#') is False or line.strip() == '']

    if clean_lines == []:
        return DRC_EMPTY_FILE_MSG
    if no_of_lines == 1:
        return random.choice(clean_lines)
    else:
        return random.sample(clean_lines, no_of_lines)


@register.inclusion_tag('real_content/tags/drc_title.html')
def drc_title(heading_level=1, css_class='', language=''):
    u"""
    Retrieve random title.
    Uses langauge from global settings if an override is not provided.
    """
    language = get_language(language)
    titles = get_text_file(language, 'titles')

    data = {
        'title': random_lines(titles, 1),
    }

    if heading_level > 6:
        data['heading_level'] = 6
    else:
        data['heading_level'] = heading_level
    data['css_class'] = css_class
    return data


@register.inclusion_tag('real_content/tags/drc_paragraph.html')
def drc_paragraphs(no_of_paraghaphs=1, css_class='', language=''):
    u"""
    Retrieve n random paragraphs.
    Uses langauge from global settings if an override is not provided.
    """
    language = get_language(language)
    paragraphs = get_text_file(language, 'paragraphs')

    data = {
        'paragraphs': random_lines(paragraphs, no_of_paraghaphs)
    }

    data['css_class'] = css_class
    return data


@register.inclusion_tag('real_content/tags/drc_lorempixel.html')
def drc_image(width=640, height=480, category='',
    gray=False, image_id='', css_class=''):
    u"""
    Retrieve image from lorempixel.com service.
    Possible categories are:
        abstract, animals, business, cats, city, food, nightlife, fashion,
        people, nature, sports, technics, transport
    """
    data = {}
    url = u'http://lorempixel.com/'
    if gray:
        url = '{url}g/'.format(url=url)
    url = '{url}{width}/{height}/'.format(url=url, width=width, height=height)
    if category:
        url = '{url}{category}/'.format(url=url, category=category)

        # image_id can only be defined if the category was set, otherwise we
        # get black image
        if image_id and image_id <= 10:
            url = '{url}{image_id}'.format(url=url, image_id=image_id)
        else:
            # use random image_id if non was set to prevent from displaying the
            # same image over and over again
            url = '{url}{image_id}'.format(
                url=url,
                image_id=random.randrange(1, 11))

    data['url'] = url
    data['css_class'] = css_class
    return data
