# -*- coding: utf-8 -*-

from django import template

# from real_content.models import Language, Content

register = template.Library()


@register.inclusion_tag('real_content/tags/drc_title.html')
def drc_title(heading_level=1, css_class='', language=''):
    u"""
    Retrieve random title.
    Uses langauge from global settings if an override is not provided.
    """
    return
    # languages = Language.get_languages(language)

    # data = {}
    # content = Content.randoms.filter(
    #         language__in=languages,
    #         content_category=Content.CONTENT_CATEGORY.title)\
    #     .first()
    # if content:
    #     data['title'] = content.content

    # if heading_level > 6:
    #     data['heading_level'] = 6
    # else:
    #     data['heading_level'] = heading_level
    # data['css_class'] = css_class
    # return data


@register.inclusion_tag('real_content/tags/drc_paragraph.html')
def drc_paragraphs(no_of_paraghaphs=1, css_class='', language=''):
    u"""
    Retrieve n random paragraphs.
    Uses langauge from global settings if an override is not provided.
    """
    return
    # languages = Language.get_languages(language)

    # data = {}
    # content = Content.randoms.filter(
    #         language__in=languages,
    #         content_category=Content.CONTENT_CATEGORY.paragraph)\
    #     .values_list('content', flat=True)[:no_of_paraghaphs]
    # if content:
    #     data['paragraphs'] = content

    # data['css_class'] = css_class
    # return data


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
