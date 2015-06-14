# -*- coding: utf-8 -*-

from django.template import Template, Context
from django.test import TestCase

from bs4 import BeautifulSoup

from real_content.settings import DRC_MISSING_FILE_MSG, DRC_EMPTY_FILE_MSG


class TitleTagTest(TestCase):
    TEMPLATE = Template('{% load drc %} {% drc_title 2 %}')

    def test_title_shows_up(self):
        rendered = self.TEMPLATE.render(Context({}))
        soup = BeautifulSoup(rendered)
        h2_tag = soup.find('h2')

        self.assertTrue(h2_tag, 'title tag missing')
        self.assertFalse(DRC_MISSING_FILE_MSG in str(h2_tag),
            'language file missing')
        self.assertFalse(DRC_EMPTY_FILE_MSG in str(h2_tag),
            'language file empty')
        self.assertFalse(h2_tag.is_empty_element, 'title tag is empty')


class ParagraphsTagTest(TestCase):
    TEMPLATE = Template('{% load drc %} {% drc_paragraphs 2 %}')

    def test_paragraphs_show_up(self):
        rendered = self.TEMPLATE.render(Context({}))
        soup = BeautifulSoup(rendered)
        p_tags = soup.find_all('p')

        self.assertTrue(p_tags, 'paragraph tags missing')
        self.assertTrue(len(p_tags) == 2, 'not enough paragraphs')
        self.assertFalse(DRC_MISSING_FILE_MSG in str(p_tags[0]),
            'language file missing')
        self.assertFalse(DRC_EMPTY_FILE_MSG in str(p_tags[0]),
            'language file empty')
        self.assertFalse(p_tags[0].is_empty_element, 'paragraph tag is empty')


class ImageTagTest(TestCase):
    TEMPLATE = Template('{% load drc %} {% drc_image 300 200 "sport" %}')

    def test_image_shows_up(self):
        rendered = self.TEMPLATE.render(Context({}))
        soup = BeautifulSoup(rendered)
        img_tag = soup.find('img')

        self.assertTrue(img_tag, 'image tag missing')
        img_source = img_tag.attrs.get('src')
        self.assertTrue('300/200' in img_source, 'wrong image dimensions')
        self.assertTrue('300/200/sport' in img_source, 'wrong image category')
