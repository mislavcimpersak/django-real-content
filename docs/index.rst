.. django-real-content documentation master file, created by
   sphinx-quickstart on Sun Jun 14 13:31:41 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-real-content's documentation!
===============================================

Django real content is a collection of template tags to quickly show real content instead of misleading `lorem ipsum <http://www.smashingmagazine.com/2010/01/06/lorem-ipsum-killing-designs/>`__.
Useful to get a sense of real world content with fun local unicode
characters.

You can view the source code for the project on `Github <https://github.com/mislav.cimpersak/django-real-content>`__.


Contents:
---------

.. toctree::
   :maxdepth: 2

   Usage <usage>
   Advanced <advanced>


Installation
============
You can get Django real content by using pip

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
--------------------------------------------

- cz, de, en, es, fr, gr, hr, it, nl, pl, rs, ru, si
