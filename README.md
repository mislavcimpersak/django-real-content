# django-real-content

Template tags to quickly show real content instead of lorem ipsum.

## Installation
```
pip install -e git+https://github.com/mislavcimpersak/django-real-content#egg=django-real-content
```

Add "real_content" to your INSTALLED_APPS setting and `DRC_LANGUAGE` setting (if none is set, english will be used).
```
INSTALLED_APPS = (
        ...
        'real_content',
    )

DRC_LANGUAGE = 'hr'
```

and run migrations
```
python manage.py migrate real_content
```

## Usage:
Load django-real-content in your template.
```
{% load drc %}
```

#### random title
show random title
```
{% drc_title %}
```
show random title using `h3` html tag
```
{% drc_title 3 %}
```
show random title using `h3` html tag and with additional css class
```
{% drc_title 3 'custom_css_class' %}
```
show random title with additional css class
```
{% drc_title css_class='custom_css_class' %}
```

#### random paragraphs
show 1 random paragraph
```
{% drc_paragaphs %}
```
show 3 random paragraphs
```
{% drc_paragaphs 3 %}
```
show 3 random paragraphs with additional css class
```
{% drc_paragaphs 3 'custom_css_class' %}
```
show 1 random paragraph with additional css class
```
{% drc_paragaphs css_class='custom_css_class' %}
```

#### random images
show random image from lorempixel.com
```
{% drc_image %}
```
show random image from lorempixel.com which dimensions are 420x360
```
{% drc_image 420 360 %}
```
show random image from lorempixel.com which dimensions are 420x360 in category "cats" and grayscale
```
{% drc_image 420 360 category='sports' gray=True %}
```

## Need more content?
Use management command `drc_addcontent` to collect titles and paragraphs from given url.
If no language is provided, it will use the one given in settings.

```
python manage.py drc_addcontent -u http://www.24sata.hr/a-383985 -l hr
```

## Content sources

Currently there are ~20 titles and ~100 paragraphs with variable lengths per language. Initial content was taken from random Wikipedia articles (featured articles of the day / latest improved articles).

- hr: http://hr.wikipedia.org
- en: http://en.wikipedia.org

## TODO
- switch from having migrations to loading from file
- refactor management command to more easily add new languages and to add lines to existing ones
- add more languages (de...)
- tests
- submit to pypi
- force lorem pixel tag shows different images (make it to show random numbered image)