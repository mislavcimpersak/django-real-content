Advanced
========

Need more content?
------------------

Use management command ``drc_addcontent`` to collect titles and
paragraphs from given url. If no language is provided, it will use the
one given in settings.

::

    python manage.py drc_addcontent -u http://www.24sata.hr/a-383985 -l hr

Bare in mind that not all pages are structured ideally so unfortunately some trash could end up in language files.

Contributing
-------------
Want to add more languages?
Open an issue and I'll do my best. Or use github's push requests or you can even just e-mail them to me.

Want to remove a title or a paragraph from some language files? Open an issue or a push request.
