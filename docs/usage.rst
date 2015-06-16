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

show random title using ``h3`` html tag with additional css class and language explicitly set (if you don't set language explicitly, tag will use language setting from your django project's settings)

::

    {% drc_title 3 css_class='custom_css_class' language='si' %}


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

show 3 random paragraphs with additional css class and language explicitly set (if you don't set language explicitly, tag will use language setting from your django project's settings)

::

    {% drc_paragraphs 3 css_class='custom_css_class' language='si' %}


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


random number
-----------------

show a random number (it's minimum and maximum values are set in DRC_NUMBER_START and DRC_NUMBER_END settings)

::

    {% drc_number %}

show a random number between 1 and 100

::

    {% drc_number 1 100 %}
