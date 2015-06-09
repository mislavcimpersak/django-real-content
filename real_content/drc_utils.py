# -*- coding: utf-8 -*-

import codecs
from datetime import datetime
import os

import urllib2
from bs4 import BeautifulSoup

from real_content.settings import DRC_LANGUAGE


def get_language(language=''):
    u"""
    Gets language from settings if it wasn't explicitly provided.
    """
    if language == '' or language is None:
        language = DRC_LANGUAGE
    language = language.lower().strip()
    return language


def get_text_file(language, text_type='titles', file_open_mode='r'):
    u"""
    Gets text file for specific language.
    Used for reading and writing to a file.
    """
    content_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'content'))
    content_file_path = os.path.join(
        content_dir, '{}_{}.txt'.format(language, text_type))

    if os.path.exists(content_file_path) or 'a' in file_open_mode:
        content_file = codecs.open(content_file_path, file_open_mode, 'utf-8')
        return content_file
    else:
        return None


def save_content(content, tag, text_type='paragraphs', url='', language='',
    min_length=150):
    u"""
    Saves content to language file.
    """
    new_data = []

    for tag in content.find_all(tag):
        new_content = ' '.join(
            [part.strip() for part in tag.getText().split('\n')]).strip()

        if len(new_content) > min_length:
            new_data.append(new_content)

    # getting rid of duplicates in new data
    new_data = list(set(new_data))

    # remove previously existing items from new data
    existing_file = get_text_file(language, text_type, 'r')
    if existing_file:
        existing_data = existing_file.read().splitlines()
    else:
        existing_data = []

    new_data_copy = new_data[:]
    for text in new_data_copy:
        if text in existing_data:
            new_data.remove(text)

    # put date and source as comments at the beginning of new data
    if len(new_data) > 0:
        new_data.insert(0, '# {}'.format(url))
        new_data.insert(0, '# {}'.format(datetime.now().isoformat()))

    # write line from new_data one by one into local file
    with get_text_file(language, text_type, 'a') as text_file:
        for new_content in new_data:
            text_file.write(u'{}\n'.format(new_content))
        text_file.write(u'\n')


def parse_url(url, language=''):
    u"""
    Getting url, parsing it and saving the contents of it to local files.
    """
    language = get_language(language)
    try:
        soup = BeautifulSoup(urllib2.urlopen(url).read())

        # saving paragraphs
        save_content(soup, 'p', 'paragraphs', url=url, language=language,
            min_length=150)

        # saving all headings
        for i in range(1, 7):
            heading_level = 'h{0}'.format(i)
            save_content(soup, heading_level, 'titles', url=url,
                language=language, min_length=20)
        return 'success!'

    except urllib2.HTTPError:
        return '403 error'
