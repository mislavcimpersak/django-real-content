# -*- coding: utf-8 -*-

import codecs
import os
import random

from django import template
from django.conf import settings

# from real_content.models import Language, Content

register = template.Library()


def random_lines(text_file, no_of_lines=1):
    u"""
    Gets a random line from a file ignoring lines starting with #.
    """
    lines = text_file.read().splitlines()
    clean_lines = [line for line in lines if line.startswith('#') is False]
    if clean_lines == []:
        return 'no usable lines in language file'
    if no_of_lines == 1:
        return random.choice(clean_lines)
    else:
        return random.sample(clean_lines, no_of_lines)


def get_language(language=''):
    if language == '':
        language = settings.DRC_LANGUAGE
    language = language.strip()
    return language


def get_text_file(language, text_type='titles'):
    content_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, 'content'))
    content_file = os.path.join(
        content_dir, '{}_{}.txt'.format(language, text_type))

    titles = codecs.open(content_file, 'r', 'utf-8')
    return titles


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
    """
    data = {}
    url = u'http://lorempixel.com/'
    # TODO use .format()
    if gray:
        url += 'g/'
    url += str(width) + '/' + str(height) + '/'
    if category:
        url += category + '/'
    if image_id:
        url += str(image_id)

    data['url'] = url
    data['css_class'] = css_class
    return data
