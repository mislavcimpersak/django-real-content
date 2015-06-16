===================
django-real-content
===================

Template tags to quickly show real content instead of misleading `lorem
ipsum <http://www.smashingmagazine.com/2010/01/06/lorem-ipsum-killing-designs/>`__.
Useful to get a sense of real world content with fun local unicode
characters.

Documentation
-------------
`Read the Docs <http://django-real-content.readthedocs.org/>`__

Installation
------------

::

    pip install django-real-content

In your project's settings file add ``real_content`` to your INSTALLED\_APPS setting and ``DRC_LANGUAGE`` setting (if none is set, english will be used).

::

    INSTALLED_APPS = (
        # ...
        'real_content',
    )

    DRC_LANGUAGE = 'hr'

Languages currently supported out of the box
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- cz, de, en, es, fr, gr, hr, it, nl, pl, rs, ru, si

Usage:
------

Explaind in more detail on `read the docs <http://django-real-content.readthedocs.org/>`__.

Load django-real-content in your template.

::

    {% load drc %}

random title
~~~~~~~~~~~~

show random h3 title

::

    {% drc_title 3 %}


random paragraphs
~~~~~~~~~~~~~~~~~

show 3 random paragraphs

::

    {% drc_paragraphs 3 %}


random image
~~~~~~~~~~~~~

show random image from lorempixel.com which dimensions are 420x360

::

    {% drc_image 420 360 %}


random number
~~~~~~~~~~~~~

show a random number between 1 and 100

::

    {% drc_number 1 100 %}


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

-  add more languages in the package as standard (fi, pt...)
