# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-real-content',
    version='0.1.4',
    packages=find_packages(),
    # packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    license='MIT',
    description='Template tags to quickly show real content instead of lorem ipsum.',
    long_description=README,
    url='https://github.com/mislavcimpersak/django-real-content',
    download_url='https://github.com/mislavcimpersak/django-real-content/tarball/0.1',
    author=u'Mislav Cimperšak',
    author_email='mislav.cimpersak@gmail.com',
    keywords='django real content lorem ipsum',
    install_requires=[
        'Django>=1.7',
        'beautifulsoup4>=4.3'
    ],
    # tests are on the roadmap
    # tests_require=[
    #     'Django>=1.7',
    # ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
