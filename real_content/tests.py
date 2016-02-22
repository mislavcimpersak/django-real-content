# -*- coding: utf-8 -*-

from django.template import Template, Context
from django.test import TestCase

from bs4 import BeautifulSoup

from real_content.drc_utils import (
    get_language,
    get_text_file,
    save_content,
    parse_url
    )
from real_content.settings import (
    DRC_MISSING_FILE_MSG,
    DRC_EMPTY_FILE_MSG,
    DRC_LANGUAGE
    )


class TitleTagTest(TestCase):
    def test_title_shows_up(self):
        template = Template('{% load drc %} {% drc_title 2 %}')
        rendered = template.render(Context({}))
        soup = BeautifulSoup(rendered, 'html.parser')
        h2_tag = soup.find('h2')

        self.assertTrue(h2_tag, 'title tag missing')
        self.assertFalse(DRC_MISSING_FILE_MSG in str(h2_tag),
            'language file missing')
        self.assertFalse(DRC_EMPTY_FILE_MSG in str(h2_tag),
            'language file empty')
        self.assertFalse(h2_tag.is_empty_element, 'title tag is empty')

    def test_title_multiple_words_in_param(self):
        template = Template('{% load drc %} {% drc_title "h3 data-arg" %}')
        rendered = template.render(Context({}))
        soup = BeautifulSoup(rendered, 'html.parser')
        h3_tag = soup.find('h3')

        self.assertFalse(h3_tag.has_attr('data-arg'))

    def test_title_empty_param(self):
        template = Template('{% load drc %} {% drc_title "" %}')
        rendered = template.render(Context({}))
        soup = BeautifulSoup(rendered, 'html.parser')
        h1_tag = soup.find('h1')

        self.assertTrue(h1_tag, 'title tag missing')

    def test_title_h_only_number_bigger_than_6(self):
        template = Template('{% load drc %} {% drc_title 9 %}')
        rendered = template.render(Context({}))
        soup = BeautifulSoup(rendered, 'html.parser')
        h6_tag = soup.find('h6')

        self.assertTrue(h6_tag, 'title tag missing')


class ParagraphsTagTest(TestCase):

    def test_paragraphs_show_up(self):
        template = Template('{% load drc %} {% drc_paragraphs 2 %}')
        rendered = template.render(Context({}))
        soup = BeautifulSoup(rendered, 'html.parser')
        p_tags = soup.find_all('p')

        self.assertTrue(p_tags, 'paragraph tags missing')
        self.assertTrue(len(p_tags) == 2, 'not enough paragraphs')
        self.assertFalse(DRC_MISSING_FILE_MSG in str(p_tags[0]),
            'language file missing')
        self.assertFalse(DRC_EMPTY_FILE_MSG in str(p_tags[0]),
            'language file empty')
        self.assertFalse(p_tags[0].is_empty_element, 'paragraph tag is empty')

    def test_paragraphs_only_one_p(self):
        template = Template('{% load drc %} {% drc_paragraphs 1 %}')
        rendered = template.render(Context({}))
        soup = BeautifulSoup(rendered, 'html.parser')
        p_tags = soup.find_all('p')

        self.assertTrue(p_tags, 'paragraph tags missing')
        self.assertTrue(len(p_tags) == 1, 'not enough paragraphs')


class ImageTagTest(TestCase):
    def test_image_shows_up(self):
        template = Template('{% load drc %} {% drc_image 300 200 "sport" %}')
        rendered = template.render(Context({}))
        soup = BeautifulSoup(rendered, 'html.parser')
        img_tag = soup.find('img')

        self.assertTrue(img_tag, 'image tag missing')
        img_source = img_tag.attrs.get('src')
        self.assertTrue('300/200' in img_source, 'wrong image dimensions')
        self.assertTrue('300/200/sport' in img_source, 'wrong image category')

    def test_image_gray(self):
        template = Template('{% load drc %} {% drc_image 300 200 gray=True %}')
        rendered = template.render(Context({}))
        soup = BeautifulSoup(rendered, 'html.parser')
        img_tag = soup.find('img')

        img_source = img_tag.attrs.get('src')
        self.assertTrue('/g/' in img_source, 'image not in grayscale')

    def test_image_specific_id(self):
        template = Template(
            '{% load drc %} {% drc_image category="people" image_id=2 %}')
        rendered = template.render(Context({}))
        soup = BeautifulSoup(rendered, 'html.parser')
        img_tag = soup.find('img')

        img_source = img_tag.attrs.get('src')
        self.assertTrue('/people/2' in img_source, 'specific image id not set')


class NumberTagTest(TestCase):
    def test_number_shows_up(self):
        template = Template('{% load drc %} {% drc_number 1 100 %}')
        rendered = template.render(Context({}))
        number = int(rendered)
        self.assertTrue(1 <= number <= 100, 'number out of bounds')

    def test_number_value_error(self):
        template = Template('{% load drc %} {% drc_number 1 "nope" %}')
        rendered = template.render(Context({}))

        self.assertEqual(rendered.strip(),
            'please provide a number as an argument',
            'argument of wrong type passed')

    def test_number_when_2nd_number_bigger_than_1st(self):
        template = Template('{% load drc %} {% drc_number 100 1 %}')
        rendered = template.render(Context({}))
        number = int(rendered)
        self.assertTrue(1 <= number <= 100, 'number out of bound')


class GetLanguage(TestCase):
    def test_get_language(self):
        self.assertEqual(DRC_LANGUAGE, get_language())
        self.assertNotEqual('hr', get_language())
        self.assertEqual('hr', get_language('hr'))


class GetTextFileTest(TestCase):
    def test_existing_file(self):
        text_file = get_text_file('en')
        self.assertIsNotNone(text_file)
        self.assertTrue(hasattr(text_file, 'read'))

    def test_nonexisting_file(self):
        text_file = get_text_file('xyz')
        self.assertIsNone(text_file)


class SaveContentTest(TestCase):
    def setUp(self):
        content = (
                '<!DOCTYPE html>'
                '<html>'
                '<body>'
                '<h1>My First Heading</h1>'
                '<p>My first paragraph.</p>'
                '<p>My second paragraph.</p>'
                '<h2>My Second Heading</h2>'
                '<p>My third paragraph.</p>'
                '</body>'
                '</html>'
            )
        self.soup = BeautifulSoup(content, 'html.parser')
        self.lang = 'test_lang'

        # deleting the old file from previous tests
        import os
        content_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'content'))
        content_file_path = os.path.join(
            content_dir, '{}_{}.txt'.format(self.lang, 'paragraphs'))
        os.remove(content_file_path)

    def test_save(self):
        save_content(self.soup, 'p', text_type='paragraphs',
            url='www.example.com', language=self.lang, min_length=10)

        text_file = get_text_file(self.lang, text_type='paragraphs')
        self.assertIsNotNone(text_file)
        self.assertTrue(hasattr(text_file, 'read'))

        lines = text_file.read().splitlines()
        clean_lines = [line for line in lines
            if line.startswith('#') is False and line.strip() != '']
        self.assertEqual(len(clean_lines), 3)

        self.assertTrue(any(line for line in lines
            if line.startswith('# www.example.com')))


class ParseUrl(TestCase):
    def setUp(self):
        self.real_url = 'https://www.yahoo.com'
        self.fake_url = 'http://www.jibber-jabber-asdasdasd-asffgdsgg.com'
        self.lang = 'test_lang'

    def test_parse_url(self):
        result = parse_url(self.real_url, self.lang)
        self.assertEqual(result, 'success!')

        result = parse_url(self.fake_url, self.lang)
        self.assertEqual(result, 'error getting content from url')
