# django-real-content

Template tags to quickly show real content instead of lorem ipsum.

*** still broken  - don't use just yet ;) ***

## instalation
```
pip install -e git+https://github.com/mislavcimpersak/django-real-content#egg=django-real-content
python manage.py migrate django-real-content
```

Add "real_content" to your INSTALLED_APPS setting
```
INSTALLED_APPS = (
        ...
        'real_content',
    )
```

## usage:

##### random title
show random title
```
{% realcontent_title %}
```
show random title using `h3` html tag
```
{% realcontent_title 3 %}
```
show random title using `h3` html tag and with additional css class
```
{% realcontent_title 3 'custom_css_class' %}
```
show random title with additional css class
```
{% realcontent_title css_class='custom_css_class' %}
```

##### random paragraphs
show 1 random paragraph
```
{% realcontent_paragaphs %}
```
show 3 random paragraphs
```
{% realcontent_paragaphs 3 %}
```
show 3 random paragraphs with additional css class
```
{% realcontent_paragaphs 3 'custom_css_class' %}
```
show 1 random paragraph with additional css class
```
{% realcontent_paragaphs css_class='custom_css_class' %}
```

##### random images
show random image from lorempixel.com
```
{% realcontent_image %}
```
show random image from lorempixel.com which dimensions are 420x360
```
{% realcontent_image 420 360 %}
```
show random image from lorempixel.com which dimensions are 420x360 in category "cats" and grayscale
```
{% realcontent_image 420 360 category='sports' gray=True %}
```

## Need more content?
Use management command `realcontent_addcontent` to collect titles and paragraphs from given url.
If no language is provided, it will use the one given in settings.

```
python manage.py realcontent_addcontent -u http://www.24sata.hr/a-383985 -l hr
```

## Content sources

Currently there are 20 titles and 100 paragraphs with variable lengths per language. Initial content was taken from random Wikipedia articles (featured articles of the day / latest improved articles).

- hr: http://hr.wikipedia.org
- en: http://en.wikipedia.org
