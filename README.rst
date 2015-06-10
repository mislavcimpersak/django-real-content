===================
django-real-content
===================

Template tags to quickly show real content instead of misleading `lorem
ipsum <http://www.smashingmagazine.com/2010/01/06/lorem-ipsum-killing-designs/>`__.
Useful to get a sense of real world content with fun local unicode
characters.

Installation
------------

::

    pip install django-real-content

Add "real\_content" to your INSTALLED\_APPS setting and ``DRC_LANGUAGE``
setting (if none is set, english will be used).

::

    INSTALLED_APPS = (
        ...
        'real_content',
    )

    DRC_LANGUAGE = 'hr'

Languages currently supported out of the box
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

de, en, hr, si

Usage:
------

Load django-real-content in your template.

::

    {% load drc %}

random title
~~~~~~~~~~~~

show random title

::

    {% drc_title %}

show random title using ``h3`` html tag

::

    {% drc_title 3 %}

show random title using ``h3`` html tag and with additional css class

::

    {% drc_title 3 'custom_css_class' %}

show random title with additional css class

::

    {% drc_title css_class='custom_css_class' %}

random paragraphs
~~~~~~~~~~~~~~~~~

show 1 random paragraph

::

    {% drc_paragraphs %}

show 3 random paragraphs

::

    {% drc_paragraphs 3 %}

show 3 random paragraphs with additional css class

::

    {% drc_paragraphs 3 'custom_css_class' %}

show 1 random paragraph with additional css class

::

    {% drc_paragraphs css_class='custom_css_class' %}

random images
~~~~~~~~~~~~~

show random image from lorempixel.com

::

    {% drc_image %}

show random image from lorempixel.com which dimensions are 420x360

::

    {% drc_image 420 360 %}

show random image from lorempixel.com which dimensions are 420x360 in
category "cats" and grayscale

::

    {% drc_image 420 360 category='sports' gray=True %}

Need more content?
------------------

Use management command ``drc_addcontent`` to collect titles and
paragraphs from given url. If no language is provided, it will use the
one given in settings.

::

    python manage.py drc_addcontent -u http://www.24sata.hr/a-383985 -l hr

Content sources
---------------

Various localised news portals and local wikipedia in some cases.

TODO
----

-  add more languages in the package as standard (cz, fr, nl...)
-  tests
-  submit to pypi
