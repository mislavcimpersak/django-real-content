Usage
=====

Load django-real-content in your template.

::

    {% load drc %}

random title
------------

show random title

::

    {% drc_title %}

show random title using ``h3`` html tag

::

    {% drc_title 3 %}

show random title with additional css class

::

    {% drc_title css_class='custom_css_class' %}

show random title using ``h3`` html tag and with additional css class

::

    {% drc_title 3 css_class='custom_css_class' %}


random paragraphs
-----------------

show 1 random paragraph

::

    {% drc_paragraphs %}

show 3 random paragraphs

::

    {% drc_paragraphs 3 %}

show 1 random paragraph with additional css class

::

    {% drc_paragraphs css_class='custom_css_class' %}

show 3 random paragraphs with additional css class

::

    {% drc_paragraphs 3 css_class='custom_css_class' %}


random image
-------------

show random image from `lorempixel.com <http://lorempixel.com>`_

::

    {% drc_image %}

show random image from lorempixel.com which dimensions are 420x360

::

    {% drc_image 420 360 %}

show random image from lorempixel.com which dimensions are 420x360 in
category "cats" and grayscale

::

    {% drc_image 420 360 category='cats' gray=True %}

show random image from lorempixel.com which dimensions are 420x360 in
category "cats", grayscale and with additional css class

::

    {% drc_image 420 360 category='sports' gray=True css_class='custom_css_class' %}
